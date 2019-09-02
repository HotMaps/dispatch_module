
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
        temperature_radiation,message = get_temperature_and_radiation(p)
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

    # output geneneration of the output
    if solution !=-1:
        list_of_tuples = [
                    dict(type="bar",label="Thermal Generation Mix"),
                    dict(type="pie",label="Thermal Generation Mix"),
                    dict(type="bar",label="Full Load Hours"),
#                    dict(type="line",label="Heat Price"),
                    ]
        graphics = [ dict( type = x["type"],
                           data = dict( labels = solution["Technologies"] if x["type"]!="line" else [x["label"]],
                                        datasets = [ dict(label=x["label"], 
                                                          data = solution[x["label"]])] )) for x in list_of_tuples]
        result = dict()
        result['name'] = CM_NAME
        result['indicator'] = [{"unit": "EUR", "name": "Anual Total Costs","value":solution['Anual Total Costs']}]
        result['graphics'] = graphics
        result['vector_layers'] = []
        result['raster_layers'] = []

    else:
        graphics = []
        result = dict()
        result['indicator'] = [{"unit": " ", "name": "Error Notification","value":message}]
        
    print(graphics)
    print("calculation finished")
    print(f"Errors:{message}")
    return result


def colorizeMyOutputRaster(out_ds):
    ct = gdal.ColorTable()
    ct.SetColorEntry(0, (0,0,0,255))
    ct.SetColorEntry(1, (110,220,110,255))
    out_ds.SetColorTable(ct)
    return out_ds
