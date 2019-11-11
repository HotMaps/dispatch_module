# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:52:40 2018

@author: root
"""
import numpy as np
import os,sys,pickle
import pandas as pd
from .mydecorator import decore_message

path2data = os.path.split(os.path.abspath(__file__))[0]
init_data = os.path.join(path2data,"data.xlsx")
path_inputs_parameter = os.path.join(path2data,"INPUTS_CALCULATION_MODULE.xlsx")

#%%
@decore_message
def get_user_input(inputs_parameter_selection,nuts,path=path_inputs_parameter):
    df = pd.read_excel(path)
    out = dict()
    for val in set(df.input_parameter_name):
        tec,key = val.split("_")
        tec = tec.strip()
        key = key.strip()
        try:
            out[key] = {**out.get(key,{}),**{tec:float(inputs_parameter_selection[val])}}
        except:
            out[key] = {**out.get(key,{}),**{tec:inputs_parameter_selection[val]}}
    for k in ["pCO2","ir","if"]:
        out = {**out,**out.pop(k)}
    list_of_tuples = [(("electricity_price_t","price_profiles"),(nuts[0],2015)),
                      (("sale_electricity_price_t","price_profiles"),(nuts[0],2015)),
                      (("demand_th_t","load_profiles"),(nuts[2],2010)),
                      ]
    out,message = load_init_profiles(out,list_of_tuples) #TODO: adapt to selcted region
    return out,message
#%%
@decore_message
def load_init_profiles(out,list_of_tuples):
    for (name1,name2),data in list_of_tuples:
        profile, message = return_dict(name2,data)
        if profile ==-1:
            return -1,message
        else:
            out[name1]= profile
    return out,None

@decore_message
def return_dict(name_dat,init_data):
    """
    This function loads "pickle" data and converts the data into dictionary
    with one-based indexing for "pyomo"

    Parameters:
        name:           string
                        name of the "dat" file :
                            i.e: "pirces" for the <prices.dat>-file

        init_data:      tuple
                        key for the data to load: i.e: ("Wien",2016)
    Returns:
        one-based-dictionary:   dict
                                This will be converted data to a
                                one-based indexed dictionary

    """
    with open(os.path.join(path2data,name_dat+".dat"),"rb") as file:
        val = pickle.load(file)[init_data]
    return dict(zip(range(1,8760+1),val.tolist())),None
#%%
@decore_message
def reshape_profile(scale_value,data,name="demand_th_t"):
    x=np.array(list(data[name].values()))
    x = x / sum(x) * scale_value
    data[name] = dict(zip(range(1,8760+1),x.tolist()))
    del x
    return data,None
#%%
@decore_message
def preprocessing(data,inv_flag):
    tec =       ["hp","st","wi","chp","hb"]
    j_hp =      ["hp"]
    j_st =      ["st"]
    j_waste =   ["wi"]
    j_chp =     ["chp"]
    j_bp =      ["hb"]

    mapper = dict(zip (tec,
                         ["Heat Pump","Solar Thermal Plant",
                          "Waste Inceneration Pant","CHP","Heat Boiler"]
                         )
                    )
    


    
    demand_th_t =           data["demand_th_t"]
    #%
    max_demad =             max(demand_th_t.values())
    max_installed_caps =    sum([data["cap"][key] for key in tec])
    ok_flag = True
    if (max_installed_caps <= max_demad) and not inv_flag:
        ok_flag = False
    
    radiation_t =                   data["radiation_t"]
    electricity_price_t =           data["electricity_price_t"]
    sale_electricity_price_t =      data["sale_electricity_price_t"]
    temperature_t =                 data["temperature_t"]
    
    
    OP_fix_j =              {mapper[key]:data["opexFix"][key] for key in tec}
    OP_var_j =              {mapper[key]:data["opexVar"][key] for key in tec}
    n_el_j =                {mapper[key]:data["nel"][key] for key in tec}
    
    mc = {}
    for j in tec:
        if data["nth"][j]  == 0:
            for t in range(1,8760+1):
                mc[j,t]= 1e100
        else:
            if data["ec"][j] == "electricity":
                for t in range(1,8760+1):
                    mc[j,t]= electricity_price_t[t] / data["nth"][j] + \
                                 data["ef"][data["ec"][j]]*data["pCO2"] / \
                                  data["nth"][j]
            else:
                for t in range(1,8760+1):
                    mc[j,t]= data["p"][data["ec"][j]] /  \
                                data["nth"][j] + \
                                 data["ef"][data["ec"][j]]*data["pCO2"] / \
                                  data["nth"][j]
    mc_jt =                 {(mapper[key],t):mc[key,t] for t in range(1,8760+1) for key in tec}
    n_th_j =                {mapper[key]:data["nth"][key] for key in tec}
    x_th_cap_j =            {mapper[key]:data["cap"][key] for key in tec}

    # Ramping Costs
    c_ramp_chp =            100
    c_ramp_waste =          100

    
    thresh = -20
    all_heat_geneartors = tec    

    IK_j = {mapper[key]:data["ic"][key] for key in tec}
    lt_j = {mapper[key]:data["lt"][key] for key in tec}
    
    ir = data["ir"]  # interest Rate
    q = 1+ir
    alpha = {}
    for ix,val in data["lt"].items():
        if val == 0 or val != val:
            alpha[ix] = 1
        else:
            alpha[ix] =  ( q**val * ir) / ( q**val - 1)

    alpha_j = {mapper[key]:alpha[key] for key in tec}
    
    tec =       ["Heat Pump","Solar Thermal Plant","Waste Inceneration Pant","CHP","Heat Boiler"]    
    j_hp =      ["Heat Pump"]
    j_st =      ["Solar Thermal Plant"]
    j_waste =   ["Waste Inceneration Pant"]
    j_chp =     ["CHP"]
    j_bp =      ["Heat Boiler"]
    
    max_rad = max(radiation_t.values())
    args = [tec, j_hp, j_st, j_waste, j_chp, j_bp, demand_th_t, max_demad, 
            radiation_t, OP_fix_j, n_el_j, electricity_price_t, mc_jt, n_th_j,
            x_th_cap_j,c_ramp_chp, c_ramp_waste, OP_var_j, temperature_t, thresh,
            sale_electricity_price_t,all_heat_geneartors,IK_j,lt_j,ir,alpha_j,max_rad]
    
    keys = ['j', 'j_hp', 'j_st', 'j_waste', 'j_chp', 'j_bp', 'demand_th_t', 'max_demad', 
            'radiation_t', 'OP_fix_j', 'n_el_j', 'electricity_price_t', 'mc_jt', 'n_th_j', 
            'x_th_cap_j', 'c_ramp_chp', 'c_ramp_waste', 'OP_var_j', 'temperature_t', 'thresh', 
            'sale_electricity_price_t', 'all_heat_geneartors',"IK_j","lt_j","ir","alpha_j","max_rad"]
    
    val = dict(zip(keys,args))
    
    #% reshape data to fit the pyomo data structure for abstract models
    pyomo_data = {}
    for key,value in val.items():
        if type(value) != dict:
            pyomo_data[key]={None:value}
        else:
            pyomo_data[key]=value
        
    pyomo_data = {None:pyomo_data} if ok_flag else -1
    
    message = None if ok_flag else f"The installed capacities are not enough to cover the load, (max_demand: {str(max_demad)} & installed cap:{str(max_installed_caps)})"    
    
    
    return pyomo_data,message
if __name__ == "__main__":
    print('Main: preprocessing Module')