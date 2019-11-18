# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:16:18 2018

@author: root
"""
import numpy as np

from .mydecorator import decore_message

def add_energy_carrier_key(key,solution,instance):
    key_new = f"{key} by Energy carrier"
    solution[key_new] = dict()
    for j in instance.j:
        solution[key_new][instance.ec_j[j]] = solution[key_new].get(instance.ec_j[j],0) + solution[key][j]
    solution[key_new] = {i:round(v,2) for i,v in solution[key_new].items()}       
@decore_message
def solution2json(instance,results,inv_flag):
# =============================================================================
#   Define Units
# =============================================================================
    units = {}
    units["Thermal Power Energymix"]= "MWh"
    units["Installed Capacities"]= "MW"
    units["Heat Price"]= "EUR/MWh"
    units["Electricity Production by CHP"]= "MWh/yr"
    units["Thermal Production by CHP"]= "MWh"
    units["Thermal Generation Mix"]= "MWh/yr"
    units["Revenue From Electricity"] = "EUR/yr"
    units["Heat Demand"] = "EUR"
    units["Electricity Price"] = "EUR/MWh"
    units["Mean Value Heat Price"] = "EUR/MWh"
    units["Median Value Heat Price"] = "EUR/MWh"
    units["O&M Cost"]=  "EUR/yr"
    units["Variable Cost CHP's"]= "EUR/yr"
    units["Fuel Costs"] = "EUR/yr"
    units["Marginal Costs"] = "EUR/MWh"        
    units["Anual Total Costs (from optimization)"] = "EUR/yr" 
    units["Ramping Costs"] = "EUR/yr"
    units["Technologies"] = ""
    units["Marginal Costs CHP"] = "EUR/MWh"
    units["Full Load Hours"] = "h"
    units["Anual Investment Cost"] = "EUR/yr" 
    units["Anual Investment Cost (of existing power plants)"] = "EUR/yr"
    units["Investment Cost (with existing power plants)"] = "EUR/yr" 
    units["Total O&M Costs"] = "EUR/yr"  
    units["Total Investment Costs"] = "EUR/yr"  
    units["Total Thermal Generation"] = "MWh/yr"
    units["Total Electricty Consumption"] = "MWh/yr" 
    units["Total Fuel Costs"] = "EUR/yr"  
    units["Total CO2 Costs"] = "EUR/yr"    
    units["LCOH"] = "EUR/MWh"
    units["CO2 Costs"] = "EUR/yr"
    units["CO2 Emissions"] = "t/yr"
    units["Total CO2 Emissions"] = "t/yr"
    units["Total Revenue From Electricity"] = "EUR/yr"
    units["Total Heat Demand"] = "MWh/yr"
    units["Total LCOH"] = "EUR/MWh"
    units["Anual Total Costs"] = "EUR/yr"
    units["Electricity Generation Mix"] = "MWh/yr"
    units["Total Electricity Generation"] = "MWh/yr"
    units["Total Ramping Costs"] = "EUR/yr"
    units['CO2 Emissions by Energy carrier'] = "t/yr"
    units['Thermal Generation Mix by Energy carrier'] ="MWh/yr"
    units["Fuel Demand"] = "MWh/yr",
    units['Final Energy Demand by Energy carrier'] = "MWh/yr"
# =============================================================================
#   Define outputs
# =============================================================================
    solution = {}    
    solution["Thermal Power Energymix"]={j:[round(instance.x_th_jt[(j,t)](),2) for t in instance.t] for j in instance.j}
    solution["Installed Capacities"]= {j:round(instance.Cap_j[j](),2) for j in instance.j}
    solution["Heat Price"]= [round(results.solution(0).constraint["genearation_covers_demand_t["+str(t)+"]"]["Dual"],2) for t in instance.t]
    solution["Electricity Production by CHP"]= round(sum([instance.x_el_jt[(j,t)]() for j in instance.j_chp for t in instance.t]),2)
    solution["Electricity Generation Mix"]= {j:round(sum([instance.x_el_jt[(j,t)]() for t in instance.t]),2) for j in instance.j}
    solution["Thermal Production by CHP"]= round(sum([instance.x_th_jt[(j,t)]() for j in instance.j_chp for t in instance.t]),2)
    solution["Thermal Generation Mix"]= {j:round(sum([instance.x_th_jt[(j,t)]() for t in instance.t]),2) for j in instance.j}
    solution["Revenue From Electricity"] = {j:round(sum(instance.x_el_jt[j,t]()*instance.sale_electricity_price_t[t] for t in instance.t),2) for j in instance.j}
    solution["Heat Demand"] = [round(instance.demand_th_t[t],2) for t in instance.t]
    solution["Electricity Price"] = [round(instance.electricity_price_t[t],2) for t in instance.t]
    solution["Mean Value Heat Price"] = round(np.mean(np.array(solution["Heat Price"])),2)
    solution["Median Value Heat Price"] = round(np.median(np.array(solution["Heat Price"])),2)
    solution["O&M Cost"]= {j:round((instance.Cap_j[j]() * instance.OP_fix_j[j] + sum(instance.x_th_jt[j,t]() * instance.OP_var_j[j]for t in instance.t)),2)for j in instance.j}
    solution["Variable Cost CHP's"]= round(sum([instance.mc_jt[j,t] * instance.x_th_jt[j,t]() - instance.sale_electricity_price_t[t] * instance.x_el_jt[j,t]() for j in instance.j_chp for t in instance.t]),2)
    solution["Fuel Costs"] = {j:round(sum([(instance.mc_jt[j,t]-instance.em_j[j]*instance.pco2/instance.n_th_j[j]) * instance.x_th_jt[j,t]() for t in instance.t]),2) for j in instance.j}  
    solution["Marginal Costs"] = {j:[round(instance.mc_jt[j,t],2) for t in instance.t] for j in instance.j}        
    solution["CO2 Costs"]= {j:round(sum([(instance.em_j[j]*instance.pco2/instance.n_th_j[j]) * instance.x_th_jt[j,t]() for t in instance.t]),2) for j in instance.j}
    solution["CO2 Emissions"]= {j:round(sum([instance.em_j[j] / instance.n_th_j[j] * instance.x_th_jt[j,t]() for t in instance.t]),2) for j in instance.j}
    solution["Anual Total Costs (from optimization)"] = round(instance.cost(),2)
    _c_ramp_waste = {j:round(sum(instance.ramp_j_waste_t[j,t]() * instance.c_ramp_waste for t in instance.t),2) for j in instance.j_waste}
    _c_ramp_chp = {j: round(sum(instance.ramp_j_chp_t[j,t]() * instance.c_ramp_chp for t in instance.t),2) for j in instance.j_chp}
    solution["Ramping Costs"] = { **{j:0 for j in instance.j},**_c_ramp_waste, **_c_ramp_chp}
    solution["Technologies"] = [j for j in instance.j]
    solution["Marginal Costs CHP"] = [np.mean([instance.mc_jt[j,t] for t in instance.t]) - instance.n_el_j[j]/instance.n_th_j[j] *np.mean([instance.sale_electricity_price_t[t] for t in instance.t]) if j in instance.j_chp else np.mean([instance.mc_jt[j,t] for t in instance.t]) for j in instance.j]
    for i,val in enumerate(instance.j):
        if val in instance.j_chp:
            solution["Marginal Costs CHP"][i] = solution["Marginal Costs CHP"][i] - instance.n_el_j[val]/instance.n_th_j[val]*np.mean([instance.sale_electricity_price_t[t] for t in instance.t])   
    solution["Full Load Hours"] = {j:round(solution["Thermal Generation Mix"][j]/solution["Installed Capacities"][j],2) if solution["Installed Capacities"][j]!=0 else 0 for j in instance.j}
    if inv_flag:
            solution["Anual Investment Cost"] = {j:round((instance.Cap_j[j]() - instance.x_th_cap_j[j])  * instance.IK_j[j] * instance.alpha_j[j],2) for j in instance.j}
    solution["Anual Investment Cost (of existing power plants)"] = {j:round(instance.x_th_cap_j[j] * instance.IK_j[j] * instance.alpha_j[j],2) for j in instance.j}
    solution["Investment Cost (with existing power plants)"] = {j:round(instance.Cap_j[j]()  * instance.IK_j[j] * instance.alpha_j[j],2) for j in instance.j}
    solution["Total O&M Costs"] = round(sum(solution["O&M Cost"].values()),2)  
    solution["Total Investment Costs"] = round(sum(solution["Investment Cost (with existing power plants)"].values()),2)  
    solution["Total Thermal Generation"] = round(sum(solution["Thermal Generation Mix"].values()),2)  
#    solution["Total Electricty Consumption"] = solution["Electrical Consumption of Heatpumps and Power to Heat devices"]  
    solution["Total Revenue From Electricity"] = round(sum(solution["Revenue From Electricity"].values()),2)  
    solution["Total Fuel Costs"] = round(sum(solution["Fuel Costs"].values()),2)  
    solution["Total CO2 Costs"] = round(sum(solution["CO2 Costs"].values()),2)     
    solution["LCOH"] =  {j:round((solution["Investment Cost (with existing power plants)"][j]+solution["O&M Cost"][j]+solution["Fuel Costs"][j] + solution["CO2 Costs"][j] + solution["Ramping Costs"][j] -solution["Revenue From Electricity"][j])/solution["Thermal Generation Mix"][j],2) if solution["Thermal Generation Mix"][j]>0 else "" for j in instance.j  }  
    solution["Total Ramping Costs"] = round(sum(solution["Ramping Costs"].values()),2) 
    solution["Anual Total Costs"] = round(solution["Total Investment Costs"] + solution["Total O&M Costs"] + solution["Total Fuel Costs"] + solution["Total CO2 Costs"]+solution["Total Ramping Costs"],2)
    solution["Total LCOH"] = round((solution["Anual Total Costs"]- solution["Total Revenue From Electricity"]) / solution["Total Thermal Generation"],2)
    solution["Total Heat Demand"] = round(sum(solution["Heat Demand"]),2)
    solution["Total Electricity Generation"] = round(sum(solution["Electricity Generation Mix"].values()),2) 
    solution["Total CO2 Emissions"] = round(sum(solution["CO2 Emissions"].values()),2)  
    for key in ["Thermal Generation Mix","CO2 Emissions"]:
        add_energy_carrier_key(key,solution,instance)
    
    solution["Fuel Demand"] = {j:round(solution["Thermal Generation Mix"][j] / instance.n_th_j[j],2) for j in instance.j}

    key = "Thermal Generation Mix"
    key_new = 'Final Energy Demand by Energy carrier'
    solution[key_new] = dict()
    for j in instance.j:
        solution[key_new][instance.ec_j[j]] = solution[key_new].get(instance.ec_j[j],0) + solution[key][j] / instance.n_th_j[j]
    solution[key_new] = {i:round(v,2) for i,v in solution[key_new].items()}
    
    
    solution["units"] = units
    return solution,None
if __name__ == "__main__":
    print('Main: SaveSolution Module')    