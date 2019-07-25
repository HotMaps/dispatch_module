# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:16:18 2018

@author: root
"""
import numpy as np

from .mydecorator import decore_message

@decore_message
def solution2json(instance,results,inv_flag):
    solution = {}
    solution["Thermal Power Energymix"]={j:[instance.x_th_jt[(j,t)]() for t in instance.t] for j in instance.j}
    solution["Installed Capacities"]= {j:instance.Cap_j[j]() for j in instance.j}
    solution["Heat Price"]= [results.solution(0).constraint["genearation_covers_demand_t["+str(t)+"]"]["Dual"] for t in instance.t]
    solution["Electricity Production by CHP"]= sum([instance.x_el_jt[(j,t)]() for j in instance.j_chp for t in instance.t])
    solution["Thermal Production by CHP"]= sum([instance.x_th_jt[(j,t)]() for j in instance.j_chp for t in instance.t])
    solution["Thermal Generation Mix"]= {j:sum([instance.x_th_jt[(j,t)]() for t in instance.t]) for j in instance.j}
    solution["Revenue From Electricity"] = {j:sum(instance.x_el_jt[j,t]()*instance.sale_electricity_price_t[t] for t in instance.t) for j in instance.j}
    solution["Heat Demand"] = [instance.demand_th_t[t] for t in instance.t]
    solution["Electricity Price"] = [instance.electricity_price_t[t] for t in instance.t]
    solution["Mean Value Heat Price"] = np.mean(np.array(solution["Heat Price"]))
    solution["Median Value Heat Price"] = np.median(np.array(solution["Heat Price"]))
    solution["Operational Cost"]= {j:(instance.Cap_j[j]() * instance.OP_fix_j[j] + sum(instance.x_th_jt[j,t]() * instance.OP_var_j[j]for t in instance.t))for j in instance.j}
    solution["Variable Cost CHP's"]= sum([instance.mc_jt[j,t] * instance.x_th_jt[j,t]() - instance.sale_electricity_price_t[t] * instance.x_el_jt[j,t]() for j in instance.j_chp for t in instance.t])
    solution["Fuel Costs"] = {j:sum([instance.mc_jt[j,t] * instance.x_th_jt[j,t]() for t in instance.t]) for j in instance.j}
    solution["MC"] = {j:[instance.mc_jt[j,t] for t in instance.t] for j in instance.j}        
    solution["Anual Total Costs"] = instance.cost()
    _c_ramp_waste = {j:sum(instance.ramp_j_waste_t[j,t]() * instance.c_ramp_waste for t in instance.t) for j in instance.j_waste}
    _c_ramp_chp = {j: sum(instance.ramp_j_chp_t[j,t]() * instance.c_ramp_chp for t in instance.t) for j in instance.j_chp}
    solution["Ramping Costs"] = {**_c_ramp_waste, **_c_ramp_chp}
    solution["Technologies"] = [j for j in instance.j]
    solution["Marginal Costs"] = [np.mean([instance.mc_jt[j,t] for t in instance.t]) - instance.n_el_j[j]/instance.n_th_j[j] *np.mean([instance.sale_electricity_price_t[t] for t in instance.t]) if j in instance.j_chp else np.mean([instance.mc_jt[j,t] for t in instance.t]) for j in instance.j]
    for i,val in enumerate(instance.j):
        if val in instance.j_chp:
            solution["Marginal Costs"][i] = solution["Marginal Costs"][i] - instance.n_el_j[val]/instance.n_th_j[val]*np.mean([instance.sale_electricity_price_t[t] for t in instance.t])   
    solution["Full Load Hours"] = {j:solution["Thermal Generation Mix"][j]/solution["Installed Capacities"][j] if solution["Installed Capacities"][j]!=0 else 0 for j in instance.j}
    if inv_flag:
            solution["Anual Investment Cost"] = {j:(instance.Cap_j[j]() - instance.x_th_cap_j[j])  * instance.IK_j[j] * instance.alpha_j[j] for j in instance.j}
    solution["Anual Investment Cost (of existing power plants)"] = {j:instance.x_th_cap_j[j] * instance.IK_j[j] * instance.alpha_j[j] for j in instance.j}
    return solution,None
if __name__ == "__main__":
    print('Main: SaveSolution Module')    