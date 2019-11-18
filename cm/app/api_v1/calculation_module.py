
from osgeo import gdal

from ..helper import generate_output_file_tif, create_zip_shapefiles
from ..constant import CM_NAME
import time

import numpy as np , pandas as pd
from .my_calculation_module_directory.dispatch import run
from .my_calculation_module_directory.preprocessing import preprocessing,reshape_profile,get_user_input
from .my_calculation_module_directory.saveSolution import solution2json
from .my_calculation_module_directory.raster_things import return_nuts_codes,get_max_heat_point,get_temperature_and_radiation

""" Entry point of the calculation module function"""
def calculation(output_directory, inputs_raster_selection, inputs_parameter_selection):

    
    inv_flag  = True if inputs_parameter_selection["if_if"]=="invest" else False
        
    path_nuts_id_tif = inputs_raster_selection["nuts_id_number"]

    (nuts0, nuts1, nuts2, nuts3),message  = return_nuts_codes(path_nuts_id_tif)
    
    ds = gdal.Open(inputs_raster_selection["heat"])
    # get raster band
    b = ds.GetRasterBand(1)
    hdm_sum  = b.ReadAsArray().sum()
    
    p,message = get_max_heat_point(inputs_raster_selection["heat"])
    if p != -1:
        temperature_radiation,message = get_temperature_and_radiation(p,nuts0)
    else:
        temperature_radiation= -1
    
    if temperature_radiation !=-1:
        data,message = get_user_input(inputs_parameter_selection,nuts=(nuts0, nuts1, nuts2, nuts3))
    else:
        data = -1
    if data !=-1:
        data,message = reshape_profile(hdm_sum,data) # set profile to match selected total heat demand
    else:
        data=-1

    if data !=-1:
        data= {**data,**temperature_radiation}
        data,message = preprocessing(data,inv_flag)
    if data != -1:
        (_instance,_results),message = run(data,inv_flag)
    else:
        _instance = -1
    
    if _instance != -1:
        solution,message = solution2json(_instance,_results,inv_flag)
    else:
        solution = -1
#    print(solution)

    color_blind_palette= {   3: ['#0072B2', '#E69F00', '#F0E442'],
        4: ['#0072B2', '#E69F00', '#F0E442', '#009E73'],
        5: ['#0072B2', '#E69F00', '#F0E442', '#009E73', '#56B4E9'],
        6: ['#0072B2', '#E69F00', '#F0E442', '#009E73', '#56B4E9', '#D55E00'],
        7: [   '#0072B2',
               '#E69F00',
               '#F0E442',
               '#009E73',
               '#56B4E9',
               '#D55E00',
               '#CC79A7'],
        8: [   '#0072B2',
               '#E69F00',
               '#F0E442',
               '#009E73',
               '#56B4E9',
               '#D55E00',
               '#CC79A7',
               '#000000']}
  
    # output geneneration of the output
    if solution !=-1:
        bar_graphs = ['Full Load Hours',
				'Installed Capacities',
				'LCOH',
				'Investment Cost (with existing power plants)',
				'O&M Cost',
				'Fuel Costs',
				'CO2 Costs',
				'Ramping Costs',
				'CO2 Emissions',
				'Thermal Generation Mix',
				'Electricity Generation Mix',
				'Revenue From Electricity',
                "Fuel Demand",
                'CO2 Emissions by Energy carrier',
				'Thermal Generation Mix by Energy carrier',
                'Final Energy Demand by Energy carrier']
        list_of_tuples = [ dict(type="bar",label=f"{x} ({solution['units'][x]})",key=x) for x in bar_graphs ]
        
        graphics = [ dict( xLabel="Technologies", 
                           yLabel=x["label"], 
                          type = x["type"], 
                          data = dict( labels = list(solution[x['key']]), 
                                      datasets = [ dict(  label=x["label"], 
                                                          backgroundColor = color_blind_palette[len(list(solution[x['key']]))]  , 
                                                          data = list(solution[x['key']].values()))] )) for x in list_of_tuples] 
    
        result = dict()
        result['name'] = CM_NAME
        
        
        indicator_list =['Total LCOH',
        				'Anual Total Costs',
        				'Total Revenue From Electricity',
        				'Total Thermal Generation',
        				'Total Electricity Generation',
        				'Total Investment Costs',
        				'Total O&M Costs',
        				'Total Fuel Costs',
        				'Total CO2 Costs',
        				'Total Ramping Costs',
        				'Total CO2 Emissions',
                        "Total Heat Demand","Total Final Energy Demand"]
        
        indicators = [{"unit":solution["units"][key], "name":key,"value":solution[key]} for key in indicator_list]
        indicators.append(dict(unit="-",name=f"Heat load profile and electricity price profile from folowing  NUTS-level used: {set((nuts0,nuts2))}",value=0))
        result['indicator'] = indicators
        result['graphics'] = graphics
        result['vector_layers'] = []
        result['raster_layers'] = []

    else:
        graphics = []
        result = dict()
        
        result['indicator'] = [dict(unit="-",name=f"Notification: {message}",value=0)]
        
    from pprint import pprint
    pprint(result) 
    
    return result


def colorizeMyOutputRaster(out_ds):
    ct = gdal.ColorTable()
    ct.SetColorEntry(0, (0,0,0,255))
    ct.SetColorEntry(1, (110,220,110,255))
    out_ds.SetColorTable(ct)
    return out_ds
