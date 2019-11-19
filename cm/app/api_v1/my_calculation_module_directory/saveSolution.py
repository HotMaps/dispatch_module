# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:16:18 2018

@author: root
"""
from .mydecorator import decore_message
import numpy as np
from engineering_notation import EngNumber
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def fromEngNumber(num):
    _suffix_lookup_table = {
        'p': 1e-12,
        'n': 1e-9,
        'u': 1e-6,
        'm': 1e-3,
        '': 1e0,
        'k': 1e3,
        'M': 1e6,
        'G': 1e9,
        'T': 1e12}
    try:
        eng_num=str(EngNumber(num))
    except:
        eng_num = str(num)
    if isfloat(eng_num):
        value = float(eng_num)
        suffix = ""
    else:
        value = float(eng_num[:-1])            
        suffix = eng_num[-1]
    scale = _suffix_lookup_table[suffix]            
    return value,suffix,scale

def adapt_units(string):
    string = string.replace("T M","E")
    string = string.replace("G M","P")
    string = string.replace("M M","T")
    string = string.replace("k M","G")
    string = string.replace("m M","k")
    string = string.replace("n M","m")  
    string = string.replace("u M","")
    string = string.replace("p M","u")
    return string
            
def add_energy_carrier_key(key,solution,instance):
    key_new = f"{key} by Energy carrier"
    solution[key_new] = dict()
    for j in instance.j:
        solution[key_new][instance.ec_j[j]] = solution[key_new].get(instance.ec_j[j],0) + solution[key][j]
    solution[key_new] = {i:v for i,v in solution[key_new].items()}       
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
    units["Fuel Demand"] = "MWh/yr"
    units['Final Energy Demand by Energy carrier'] = "MWh/yr"
    units["Total Final Energy Demand"] = "MWh/yr"
# =============================================================================
#   Define outputs
# =============================================================================
    solution = {}    
    solution["Thermal Power Energymix"]={j:[instance.x_th_jt[(j,t)]() for t in instance.t] for j in instance.j}
    solution["Installed Capacities"]= {j:instance.Cap_j[j]() for j in instance.j}
    solution["Heat Price"]= [results.solution(0).constraint["genearation_covers_demand_t["+str(t)+"]"]["Dual"] for t in instance.t]
    solution["Electricity Production by CHP"]= sum([instance.x_el_jt[(j,t)]() for j in instance.j_chp for t in instance.t])
    solution["Electricity Generation Mix"]= {j:sum([instance.x_el_jt[(j,t)]() for t in instance.t]) for j in instance.j}
    solution["Thermal Production by CHP"]= sum([instance.x_th_jt[(j,t)]() for j in instance.j_chp for t in instance.t])
    solution["Thermal Generation Mix"]= {j:sum([instance.x_th_jt[(j,t)]() for t in instance.t]) for j in instance.j}
    solution["Revenue From Electricity"] = {j:sum(instance.x_el_jt[j,t]()*instance.sale_electricity_price_t[t] for t in instance.t) for j in instance.j}
    solution["Heat Demand"] = [instance.demand_th_t[t] for t in instance.t]
    solution["Electricity Price"] = [instance.electricity_price_t[t] for t in instance.t]
    solution["Mean Value Heat Price"] = np.mean(np.array(solution["Heat Price"]))
    solution["Median Value Heat Price"] = np.median(np.array(solution["Heat Price"]))
    solution["O&M Cost"]= {j:(instance.Cap_j[j]() * instance.OP_fix_j[j] + sum(instance.x_th_jt[j,t]() * instance.OP_var_j[j]for t in instance.t))for j in instance.j}
    solution["Variable Cost CHP's"]= sum([instance.mc_jt[j,t] * instance.x_th_jt[j,t]() - instance.sale_electricity_price_t[t] * instance.x_el_jt[j,t]() for j in instance.j_chp for t in instance.t])
    solution["Fuel Costs"] = {j:sum([(instance.mc_jt[j,t]-instance.em_j[j]*instance.pco2/instance.n_th_j[j]) * instance.x_th_jt[j,t]() for t in instance.t]) for j in instance.j}  
    solution["Marginal Costs"] = {j:[instance.mc_jt[j,t] for t in instance.t] for j in instance.j}        
    solution["CO2 Costs"]= {j:sum([(instance.em_j[j]*instance.pco2/instance.n_th_j[j]) * instance.x_th_jt[j,t]() for t in instance.t]) for j in instance.j}
    solution["CO2 Emissions"]= {j:sum([instance.em_j[j] / instance.n_th_j[j] * instance.x_th_jt[j,t]() for t in instance.t]) for j in instance.j}
    solution["Anual Total Costs (from optimization)"] = instance.cost()
    _c_ramp_waste = {j:sum(instance.ramp_j_waste_t[j,t]() * instance.c_ramp_waste for t in instance.t) for j in instance.j_waste}
    _c_ramp_chp = {j: sum(instance.ramp_j_chp_t[j,t]() * instance.c_ramp_chp for t in instance.t) for j in instance.j_chp}
    solution["Ramping Costs"] = { **{j:0 for j in instance.j},**_c_ramp_waste, **_c_ramp_chp}
    solution["Technologies"] = [j for j in instance.j]
    solution["Marginal Costs CHP"] = [np.mean([instance.mc_jt[j,t] for t in instance.t]) - instance.n_el_j[j]/instance.n_th_j[j] *np.mean([instance.sale_electricity_price_t[t] for t in instance.t]) if j in instance.j_chp else np.mean([instance.mc_jt[j,t] for t in instance.t]) for j in instance.j]
    for i,val in enumerate(instance.j):
        if val in instance.j_chp:
            solution["Marginal Costs CHP"][i] = solution["Marginal Costs CHP"][i] - instance.n_el_j[val]/instance.n_th_j[val]*np.mean([instance.sale_electricity_price_t[t] for t in instance.t])   
    solution["Full Load Hours"] = {j:solution["Thermal Generation Mix"][j]/solution["Installed Capacities"][j] if solution["Installed Capacities"][j]!=0 else 0 for j in instance.j}
    if inv_flag:
            solution["Anual Investment Cost"] = {j:(instance.Cap_j[j]() - instance.x_th_cap_j[j])  * instance.IK_j[j] * instance.alpha_j[j] for j in instance.j}
    solution["Anual Investment Cost (of existing power plants)"] = {j:instance.x_th_cap_j[j] * instance.IK_j[j] * instance.alpha_j[j] for j in instance.j}
    solution["Investment Cost (with existing power plants)"] = {j:instance.Cap_j[j]()  * instance.IK_j[j] * instance.alpha_j[j] for j in instance.j}
    solution["Total O&M Costs"] = sum(solution["O&M Cost"].values())  
    solution["Total Investment Costs"] = sum(solution["Investment Cost (with existing power plants)"].values())  
    solution["Total Thermal Generation"] = sum(solution["Thermal Generation Mix"].values())  
#    solution["Total Electricty Consumption"] = solution["Electrical Consumption of Heatpumps and Power to Heat devices"]  
    solution["Total Revenue From Electricity"] = sum(solution["Revenue From Electricity"].values())  
    solution["Total Fuel Costs"] = sum(solution["Fuel Costs"].values())  
    solution["Total CO2 Costs"] = sum(solution["CO2 Costs"].values())     
    solution["LCOH"] =  {j:(solution["Investment Cost (with existing power plants)"][j]+solution["O&M Cost"][j]+solution["Fuel Costs"][j] + solution["CO2 Costs"][j] + solution["Ramping Costs"][j] -solution["Revenue From Electricity"][j])/solution["Thermal Generation Mix"][j] if solution["Thermal Generation Mix"][j]>0 else 0 for j in instance.j  }  
    solution["Total Ramping Costs"] = sum(solution["Ramping Costs"].values()) 
    solution["Anual Total Costs"] = solution["Total Investment Costs"] + solution["Total O&M Costs"] + solution["Total Fuel Costs"] + solution["Total CO2 Costs"]+solution["Total Ramping Costs"]
    solution["Total LCOH"] = (solution["Anual Total Costs"]- solution["Total Revenue From Electricity"]) / solution["Total Thermal Generation"]
    solution["Total Heat Demand"] = sum(solution["Heat Demand"])
    solution["Total Electricity Generation"] = sum(solution["Electricity Generation Mix"].values()) 
    solution["Total CO2 Emissions"] = sum(solution["CO2 Emissions"].values())  
    for key in ["Thermal Generation Mix","CO2 Emissions"]:
        add_energy_carrier_key(key,solution,instance)
    
    solution["Fuel Demand"] = {j:solution["Thermal Generation Mix"][j] / instance.n_th_j[j] for j in instance.j}

    key = "Thermal Generation Mix"
    key_new = 'Final Energy Demand by Energy carrier'
    solution[key_new] = dict()
    for j in instance.j:
        solution[key_new][instance.ec_j[j]] = solution[key_new].get(instance.ec_j[j],0) + solution[key][j] / instance.n_th_j[j]
    solution[key_new] = {i:v for i,v in solution[key_new].items()}
    
    solution["Total Final Energy Demand"] = sum(solution["Final Energy Demand by Energy carrier"].values()) 
    #%%
#    import pickle
#    pickle.dump([solution,units],open(r"C:\Users\hasani\Desktop\test.dat","wb"))
    #%%
#    import pickle
#    import numpy as np
#    solution,units = pickle.load(open(r"C:\Users\hasani\Desktop\test.dat","rb"))
#    from engineering_notation import EngNumber 
    
    for key,val in solution.items():
        if key == "Technologies":
            continue
        if type(val) == dict or type(val) == list:
            num=float(np.percentile(np.asarray(list(val.values()) if type(val) == dict else val).astype(float),90))
            value,suffix,scale =  fromEngNumber(num)
            units[key] = f"{suffix} {units[key]}"
            units[key] = adapt_units(units[key])

            if type(val) == dict: 
                for key2,val2 in val.items():
                    if type(val2) == list:
                        solution[key][key2] = (np.asarray(val2)/scale).round(2).tolist()
                    else:
                        solution[key][key2] = round(val2/scale,2)
            else:
                solution[key] = (np.asarray(val)/scale).round(2).tolist()
        else:
            value,suffix,scale =  fromEngNumber(val)
            solution[key] = value
            units[key] = f"{suffix} {units[key]}"
            units[key] = adapt_units(units[key])
#%%    
    solution["units"] = units
    return solution,None
if __name__ == "__main__":
    print('Main: SaveSolution Module')    