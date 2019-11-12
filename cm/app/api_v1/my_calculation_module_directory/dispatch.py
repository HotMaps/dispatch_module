# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:52:51 2017

@author: root
"""
#%% Import needed modules
import pyomo.environ as pyo
from datetime import datetime
import os
from pyomo.opt import SolverStatus, TerminationCondition
path = os.path.split(os.path.abspath(__file__))[0]
from .mydecorator import decore_message

@decore_message
def run(data,inv_flag):
    #%% Define a  Model
    m = pyo.AbstractModel()
    #%% Sets     
    m.t = pyo.RangeSet(1,8760)
    m.j = pyo.Set()
    m.j_hp = pyo.Set()
    m.j_waste = pyo.Set()
    m.j_chp = pyo.Set()
    m.j_boiler = pyo.Set()
    m.j_st = pyo.Set()
    m.all_heat_geneartors = pyo.Set()
    #%% Parameter 
    m.demand_th_t = pyo.Param(m.t)
    m.max_demad = pyo.Param()
    m.radiation_t = pyo.Param(m.t)
    m.OP_fix_j = pyo.Param(m.j)
    m.n_el_j = pyo.Param(m.j)
    m.electricity_price_jt = pyo.Param(m.j,m.t)
    m.mc_jt = pyo.Param(m.j,m.t)
    m.n_th_j = pyo.Param(m.j)
    m.x_th_cap_j = pyo.Param(m.j)
    m.c_ramp_chp = pyo.Param()
    m.c_ramp_waste = pyo.Param()
    m.OP_var_j = pyo.Param(m.j)
    m.temperature_t = pyo.Param(m.t)
    m.thresh =  pyo.Param()
    m.sale_electricity_price_t = pyo.Param(m.t)
    m.electricity_price_t = pyo.Param(m.t)
    m.IK_j = pyo.Param(m.j)
    m.alpha_j = pyo.Param(m.j)
    m.lt_j = pyo.Param(m.j)
    m.ir = pyo.Param()
    m.max_rad = pyo.Param()
    m.em_j = pyo.Param(m.j)
    m.pco2 = pyo.Param()
    #%% decision variables 
    m.x_th_jt = pyo.Var(m.j,m.t,within=pyo.NonNegativeReals)
    m.x_el_jt = pyo.Var(m.j,m.t,within=pyo.NonNegativeReals)
    m.ramp_j_chp_t = pyo.Var(m.j_chp, m.t,within=pyo.NonNegativeReals)
    m.ramp_j_waste_t = pyo.Var(m.j_waste, m.t,within=pyo.NonNegativeReals)
    m.Cap_j = pyo.Var(m.j,within=pyo.NonNegativeReals)
    #%% Constraints
    #% electircal power generation
    def gen_el_jt_rule(m,j,t):
        if m.n_th_j[j] != 0:
            return m.x_el_jt[j,t] == m.x_th_jt[j,t] / m.n_th_j[j] * m.n_el_j[j]
        else:
            return m.x_el_jt[j,t] == 0
    m.gen_el_jt = pyo.Constraint(m.j,m.t,rule=gen_el_jt_rule)

    def capacity_restriction_max_j_rule (m,j):
        #% ToDo: Define upper bound because when technologies can make revenues 
        if inv_flag:
            rule = m.Cap_j[j]  <= m.max_demad
        else:
            rule = m.Cap_j[j] == m.x_th_cap_j[j]
        return rule
    m.capacity_restriction_max_j = pyo.Constraint(m.j,rule=capacity_restriction_max_j_rule)
    
    def capacity_restriction_min_j_rule (m,j):
        return m.Cap_j[j] >= m.x_th_cap_j[j]
    m.capacity_restriction_min_j = pyo.Constraint(m.j,rule=capacity_restriction_min_j_rule)

    #% The amount of heat energy generated must not exceed the installed capacities
    def generation_restriction_jt_rule(m,j,t):
        rule = m.x_th_jt[j,t] <= m.Cap_j[j]
        return rule
    m.generation_restriction_jt = pyo.Constraint(m.j,m.t,rule=generation_restriction_jt_rule)
    
    #%  At any time, the heating generation must cover the heating demand
    def genearation_covers_demand_t_rule(m,t):
        return sum([m.x_th_jt[j,t] for j in m.j]) == m.demand_th_t[t]
    m.genearation_covers_demand_t = pyo.Constraint(m.t,rule=genearation_covers_demand_t_rule)

    #% The solar gains depend on the installed capacity and the solar radiation
    def solar_restriction_jt_rule(m,j,t):
        return m.x_th_jt[j,t] <=  m.Cap_j[j]*m.radiation_t[t]/m.max_rad
    m.solar_restriction_jt = pyo.Constraint(m.j_st,m.t,rule=solar_restriction_jt_rule)

    #% Restriction for the Heat Pumps in the cold Seasion
    def heat_pump_restriction_jt_rule(m,j,t):
        if m.temperature_t[t] <= m.thresh:
            return m.x_th_jt[j,t] == 0
        else:
            return m.x_th_jt[j,t] <=  m.max_demad
    m.heat_pump_restriction_jt = pyo.Constraint(m.j_hp,m.t,rule=heat_pump_restriction_jt_rule)
    
    def ramp_j_chp_t_rule (m,j,t):
        if t==1:
            return m.ramp_j_chp_t[j,t] == 0
        else:
            return m.ramp_j_chp_t[j,t] >= m.x_th_jt[j,t] - m.x_th_jt[j,t-1]
    m.ramping_j_chp_t = pyo.Constraint(m.j_chp,m.t,rule=ramp_j_chp_t_rule)

    def ramp_j_waste_t_rule (m,j,t):
        if t==1:
            return m.ramp_j_waste_t[j,t] == 0
        else:
            return m.ramp_j_waste_t[j,t] >= m.x_th_jt[j,t] - m.x_th_jt[j,t-1]
    m.ramping_j_waste_t = pyo.Constraint(m.j_waste,m.t,rule=ramp_j_waste_t_rule)

#   Seting cap for chp generation
    def chp_geneartion_restriction4_jt_rule(m,j,t):
        rule = m.x_th_jt[j,t] <= m.demand_th_t[t] 
        return rule
    m.chp_geneartion_restriction4_jt = pyo.Constraint(m.j_chp,m.t,rule=chp_geneartion_restriction4_jt_rule)
    
    
    #%% Objective Function
    def cost_rule(m):
        if inv_flag:
            c_inv = sum([(m.Cap_j[j] - m.x_th_cap_j[j])  * m.IK_j[j] * m.alpha_j[j] for j in m.j]) 
            c_op_fix = sum([(m.Cap_j[j]+m.x_th_cap_j[j]) * m.OP_fix_j[j] for j in m.j]) 
        else:
            c_inv = 0
            c_op_fix = sum([m.Cap_j[j] * m.OP_fix_j[j] for j in m.j]) 

        c_op_var = sum([m.x_th_jt[j,t]* m.OP_var_j[j] for j in m.j for t in m.t])

        c_var= sum([m.mc_jt[j,t] * m.x_th_jt[j,t] for j in m.j for t in m.t])
        c_ramp = sum ([m.ramp_j_waste_t[j,t] * m.c_ramp_waste for j in m.j_waste for t in m.t]) + sum ([m.ramp_j_chp_t[j,t] * m.c_ramp_chp for j in m.j_chp for t in m.t])
        c_tot = c_inv + c_var + c_op_fix + c_op_var + c_ramp 
        rev_gen_electricity = sum([m.x_el_jt[j,t]*(m.sale_electricity_price_t[t]) for j in m.j for t in m.t])
        rule = c_tot - rev_gen_electricity
        return rule
    m.cost = pyo.Objective(rule=cost_rule)
    
    #%% Compile Model
    print("*****************\nCreating Model...\n*****************")
    solv_start = datetime.now()
    instance = m.create_instance(data,report_timing= False)  #TODO
    print("*****************\ntime to create model: " + str(datetime.now()-solv_start)+"\n*****************")
    solv_start = datetime.now()
    print("*****************\nStart Solving...\n*****************")
    opt = pyo.SolverFactory("gurobi")
    results = opt.solve(instance, load_solutions=False,tee=False,suffixes=['.*'])   # tee= Solver Progress, Suffix um z.B Duale Variablen anzuzeigen -> '.*' für alle
    instance.solutions.load_from(results)
    instance.solutions.store_to(results)
    print("*****************\ntime for solving: " + str(datetime.now()-solv_start)+"\n*****************")

    if (results.solver.status == SolverStatus.ok) and (results.solver.termination_condition == TerminationCondition.optimal):
        print ("*****************\nthis is feasible and optimal"+"\n*****************")
        return(instance,results),None
    elif results.solver.termination_condition == TerminationCondition.infeasible:
        print ("*****************\nthis is infeasible or unbounded"+"\n*****************")
        return (-1,-1),"this is infeasible or unbounded"
    else:
        print ("*****************\n"+str(results.solver.termination_condition)+"\n*****************\n")
        return (-1,-1),results.solver.message       
if __name__ == "__main__":
    print('Main: Dispatch Module')
#    from disptach import run
#    from preprocessing import preprocessing,load_init_data
#    from saveSolution import solution2json
#    instance,results = run(preprocessing(load_init_data()))
#    solution = solution2json(instance,results)
  


