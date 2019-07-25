
CELERY_BROKER_URL_DOCKER = 'amqp://admin:mypass@rabbit:5672/'
CELERY_BROKER_URL_LOCAL = 'amqp://localhost/'


CM_REGISTER_Q = 'rpc_queue_CM_register' # Do no change this value

CM_NAME = 'CM - Scale heat and cool density maps'
RPC_CM_ALIVE= 'rpc_queue_CM_ALIVE' # Do no change this value
RPC_Q = 'rpc_queue_CM_compute' # Do no change this value
CM_ID = 14 # CM_ID is defined by the enegy research center of Martigny (CREM)
PORT_LOCAL = int('500' + str(CM_ID))
PORT_DOCKER = 80

#TODO ********************setup this URL depending on which version you are running***************************

CELERY_BROKER_URL = CELERY_BROKER_URL_DOCKER
PORT = PORT_DOCKER

#TODO ********************setup this URL depending on which version you are running***************************
TRANFER_PROTOCOLE ='http://'
# =============================================================================
# 
# =============================================================================

INPUTS_CALCULATION_MODULE = [{'input_name': 'Heat Boiler - Thermal Output Capacity - [MW]',
  'input_type': 'input',
  'input_parameter_name': 'hb_cap',
  'input_value': 10,
  'input_priority': 0,
  'input_unit': 'MW',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'Heat Pump - Thermal Output Capacity  - [MW]',
  'input_type': 'input',
  'input_parameter_name': 'hp_cap',
  'input_value': 20,
  'input_priority': 0,
  'input_unit': 'MW',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'Solar Thermal - Thermal Output Capacity  - [MW]',
  'input_type': 'input',
  'input_parameter_name': 'st_cap',
  'input_value': 30,
  'input_priority': 0,
  'input_unit': 'MW',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'Back Pressure CHP - Thermal Output Capacity  - [MW]',
  'input_type': 'input',
  'input_parameter_name': 'chp_cap',
  'input_value': 40,
  'input_priority': 0,
  'input_unit': 'MW',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'Waste Incineration Plant - Thermal Output Capacity - [MW]',
  'input_type': 'input',
  'input_parameter_name': 'wi_cap',
  'input_value': 50,
  'input_priority': 0,
  'input_unit': 'MW',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'Heat Boiler - thermal efficiency - [-]',
  'input_type': 'input',
  'input_parameter_name': 'hb_nth',
  'input_value': 0.875,
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 0.001,
  'input_max': 1,
  'cm_id': CM_ID},
 {'input_name': 'Heat Pump  - thermal efficiency - [-]',
  'input_type': 'input',
  'input_parameter_name': 'hp_nth',
  'input_value': 3,
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 0.001,
  'input_max': 1,
  'cm_id': CM_ID},
 {'input_name': 'Solar Thermal - thermal efficiency - [-]',
  'input_type': 'input',
  'input_parameter_name': 'st_nth',
  'input_value': 1,
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 0.001,
  'input_max': 1,
  'cm_id': CM_ID},
 {'input_name': 'Back Pressure CHP - thermal efficiency - [-]',
  'input_type': 'input',
  'input_parameter_name': 'chp_nth',
  'input_value': 0.36,
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 0.001,
  'input_max': 1,
  'cm_id': CM_ID},
 {'input_name': 'Waste Incineration Plant- thermal efficiency - [-]',
  'input_type': 'input',
  'input_parameter_name': 'wi_nth',
  'input_value': 0.36,
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 0.001,
  'input_max': 1,
  'cm_id': CM_ID},
 {'input_name': 'Heat Boiler - electrical efficiency - [-]',
  'input_type': 'input',
  'input_parameter_name': 'hb_nel',
  'input_value': 0,
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 0.001,
  'input_max': 1,
  'cm_id': CM_ID},
 {'input_name': 'Heat Pump  - electrical efficiency - [-]',
  'input_type': 'input',
  'input_parameter_name': 'hp_nel',
  'input_value': 0,
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 0.001,
  'input_max': 1,
  'cm_id': CM_ID},
 {'input_name': 'Solar Thermal - electrical efficiency - [-]',
  'input_type': 'input',
  'input_parameter_name': 'st_nel',
  'input_value': 0,
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 0.001,
  'input_max': 1,
  'cm_id': CM_ID},
 {'input_name': 'Back Pressure CHP - electrical efficiency - [-]',
  'input_type': 'input',
  'input_parameter_name': 'chp_nel',
  'input_value': 0.5,
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 0.001,
  'input_max': 1,
  'cm_id': CM_ID},
 {'input_name': 'Waste Incineration Plant- electrical efficiency - [-]',
  'input_type': 'input',
  'input_parameter_name': 'wi_nel',
  'input_value': 0.45,
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 0.001,
  'input_max': 1,
  'cm_id': CM_ID},
 {'input_name': 'Heat Boiler - energy carrier - [MW]',
  'input_type': 'select',
  'input_parameter_name': 'hb_ec',
  'input_value': "['electricity', 'gas. Biomass', 'waste', 'wood pellets', 'radiation', 'various']",
  'input_priority': 1,
  'input_unit': 'EUR/MWh',
  'input_min': 'none',
  'input_max': 'none',
  'cm_id': CM_ID},
 {'input_name': 'Heat Pump  - Capacity - [MW]',
  'input_type': 'select',
  'input_parameter_name': 'hp_ec',
  'input_value': "['electricity', 'gas. Biomass', 'waste', 'wood pellets', 'radiation', 'various']",
  'input_priority': 0,
  'input_unit': 'EUR/MWh',
  'input_min': 'none',
  'input_max': 'none',
  'cm_id': CM_ID},
 {'input_name': 'Solar Thermal - Capacity - [MW]',
  'input_type': 'select',
  'input_parameter_name': 'st_ec',
  'input_value': "['electricity', 'gas. Biomass', 'waste', 'wood pellets', 'radiation', 'various']",
  'input_priority': 4,
  'input_unit': 'EUR/MWh',
  'input_min': 'none',
  'input_max': 'none',
  'cm_id': CM_ID},
 {'input_name': 'Back Pressure CHP - Capacity - [MW]',
  'input_type': 'select',
  'input_parameter_name': 'chp_ec',
  'input_value': "['electricity', 'gas. Biomass', 'waste', 'wood pellets', 'radiation', 'various']",
  'input_priority': 3,
  'input_unit': 'EUR/MWh',
  'input_min': 'none',
  'input_max': 'none',
  'cm_id': CM_ID},
 {'input_name': 'Waste Incineration Plant- Capacity - [MW]',
  'input_type': 'select',
  'input_parameter_name': 'wi_ec',
  'input_value': "['electricity', 'gas. Biomass', 'waste', 'wood pellets', 'radiation', 'various']",
  'input_priority': 2,
  'input_unit': 'EUR/MWh',
  'input_min': 'none',
  'input_max': 'none',
  'cm_id': CM_ID},
 {'input_name': 'Heat Boiler - OPEX fix - [EUR/MW]',
  'input_type': 'input',
  'input_parameter_name': 'hb_opexFix',
  'input_value': 9000,
  'input_priority': 0,
  'input_unit': 'EUR/MW',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Heat Pump  - OPEX fix - [EUR/MW]',
  'input_type': 'input',
  'input_parameter_name': 'hp_opexFix',
  'input_value': 10000,
  'input_priority': 0,
  'input_unit': 'EUR/MW',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Solar Thermal - OPEX fix - [EUR/MW]',
  'input_type': 'input',
  'input_parameter_name': 'st_opexFix',
  'input_value': 10000,
  'input_priority': 0,
  'input_unit': 'EUR/MW',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Back Pressure CHP - OPEX fix - [EUR/MW]',
  'input_type': 'input',
  'input_parameter_name': 'chp_opexFix',
  'input_value': 34000,
  'input_priority': 0,
  'input_unit': 'EUR/MW',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Waste Incineration Plant- OPEX fix - [EUR/MW]',
  'input_type': 'input',
  'input_parameter_name': 'wi_opexFix',
  'input_value': 100000,
  'input_priority': 0,
  'input_unit': 'EUR/MW',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Heat Boiler - OPEX var - [EUR/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'hb_opexVar',
  'input_value': 1.5,
  'input_priority': 0,
  'input_unit': 'EUR/MWh',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Heat Pump  - OPEX var - [EUR/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'hp_opexVar',
  'input_value': 0.5,
  'input_priority': 0,
  'input_unit': 'EUR/MWh',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Solar Thermal - OPEX var - [EUR/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'st_opexVar',
  'input_value': 0.5,
  'input_priority': 0,
  'input_unit': 'EUR/MWh',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Back Pressure CHP - OPEX var - [EUR/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'chp_opexVar',
  'input_value': 4.5,
  'input_priority': 0,
  'input_unit': 'EUR/MWh',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Waste Incineration Plant- OPEX var - [EUR/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'wi_opexVar',
  'input_value': 0.5,
  'input_priority': 0,
  'input_unit': 'EUR/MWh',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Heat Boiler - investment cost - [EUR/MW]',
  'input_type': 'input',
  'input_parameter_name': 'hb_ic',
  'input_value': 474000,
  'input_priority': 0,
  'input_unit': 'EUR/MW',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Heat Pump  - investment cost - [EUR/MW]',
  'input_type': 'input',
  'input_parameter_name': 'hp_ic',
  'input_value': 510000,
  'input_priority': 0,
  'input_unit': 'EUR/MW',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Solar Thermal - investment cost - [EUR/MW]',
  'input_type': 'input',
  'input_parameter_name': 'st_ic',
  'input_value': 550000,
  'input_priority': 0,
  'input_unit': 'EUR/MW',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Back Pressure CHP - investment cost - [EUR/MW]',
  'input_type': 'input',
  'input_parameter_name': 'chp_ic',
  'input_value': 1300000,
  'input_priority': 0,
  'input_unit': 'EUR/MW',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Waste Incineration Plant- investment cost - [EUR/MW]',
  'input_type': 'input',
  'input_parameter_name': 'wi_ic',
  'input_value': 1200000,
  'input_priority': 0,
  'input_unit': 'EUR/MW',
  'input_min': 0,
  'input_max': 10000000,
  'cm_id': CM_ID},
 {'input_name': 'Heat Boiler - lifetime - [a]',
  'input_type': 'input',
  'input_parameter_name': 'hb_lt',
  'input_value': 21,
  'input_priority': 0,
  'input_unit': 'a',
  'input_min': 0,
  'input_max': 50,
  'cm_id': CM_ID},
 {'input_name': 'Heat Pump  -  lifetime - [a]',
  'input_type': 'input',
  'input_parameter_name': 'hp_lt',
  'input_value': 25,
  'input_priority': 0,
  'input_unit': 'a',
  'input_min': 0,
  'input_max': 50,
  'cm_id': CM_ID},
 {'input_name': 'Solar Thermal -  lifetime - [a]',
  'input_type': 'input',
  'input_parameter_name': 'st_lt',
  'input_value': 20,
  'input_priority': 0,
  'input_unit': 'a',
  'input_min': 0,
  'input_max': 50,
  'cm_id': CM_ID},
 {'input_name': 'Back Pressure CHP -  lifetime - [a]',
  'input_type': 'input',
  'input_parameter_name': 'chp_lt',
  'input_value': 25,
  'input_priority': 0,
  'input_unit': 'a',
  'input_min': 0,
  'input_max': 50,
  'cm_id': CM_ID},
 {'input_name': 'Waste Incineration Plant-  lifetime - [a]',
  'input_type': 'input',
  'input_parameter_name': 'wi_lt',
  'input_value': 20,
  'input_priority': 0,
  'input_unit': 'a',
  'input_min': 0,
  'input_max': 50,
  'cm_id': CM_ID},
 {'input_name': 'energy carrier price - electricity - [EUR/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'electricity_p',
  'input_value': 0,
  'input_priority': 1,
  'input_unit': 'EUR/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'energy carrier price - gas. Biomass - [EUR/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'biomass_p',
  'input_value': 100,
  'input_priority': 0,
  'input_unit': 'EUR/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'energy carrier price - waste - [EUR/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'waste_p',
  'input_value': 1,
  'input_priority': 0,
  'input_unit': 'EUR/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'energy carrier price - wood pellets - [EUR/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'wood_p',
  'input_value': 36,
  'input_priority': 0,
  'input_unit': 'EUR/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'energy carrier price - radiation - [EUR/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'radiation_p',
  'input_value': 0,
  'input_priority': 0,
  'input_unit': 'EUR/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'energy carrier price - various - [EUR/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'various_p',
  'input_value': 22,
  'input_priority': 0,
  'input_unit': 'EUR/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'emission factor - electricity - [tCO2/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'electricity_ef',
  'input_value': 0.8,
  'input_priority': 0,
  'input_unit': 'tCO2/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'emission factor - gas. Biomass - [tCO2/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'biomass_ef',
  'input_value': 0,
  'input_priority': 0,
  'input_unit': 'tCO2/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'emission factor  - waste - [tCO2/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'waste_ef',
  'input_value': 0.05,
  'input_priority': 0,
  'input_unit': 'tCO2/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'emission factor  - wood pellets - [tCO2/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'wood_ef',
  'input_value': 0,
  'input_priority': 0,
  'input_unit': 'tCO2/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'emission factor  - radiation - [tCO2/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'radiation_ef',
  'input_value': 0,
  'input_priority': 0,
  'input_unit': 'tCO2/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'emission factor  - various - [tCO2/MWh]',
  'input_type': 'input',
  'input_parameter_name': 'various_ef',
  'input_value': 0,
  'input_priority': 0,
  'input_unit': 'tCO2/MWh',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'CO2 Price - [EUR/tCO2]',
  'input_type': 'input',
  'input_parameter_name': 'pCO2_pCO2',
  'input_value': 25,
  'input_priority': 0,
  'input_unit': 'EUR/tCO2',
  'input_min': 0,
  'input_max': 100000,
  'cm_id': CM_ID},
 {'input_name': 'interest rate - [-]',
  'input_type': 'input',
  'input_parameter_name': 'ir_ir',
  'input_value': 0.05,
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 'none',
  'input_max': 'none',
  'cm_id': CM_ID},
 {'input_name': 'invest mode',
  'input_type': 'radio',
  'input_parameter_name': 'if_if',
  'input_value': '["invest","dispatch"]',
  'input_priority': 0,
  'input_unit': 'none',
  'input_min': 'none',
  'input_max': 'none',
  'cm_id': CM_ID}]

#from .api_v1.my_calculation_module_directory.input_widgets import load_input_widgets
#INPUTS_CALCULATION_MODULE,_ = load_input_widgets(CM_ID)


SIGNATURE = {

    "category": "Buildings",
    "cm_name": CM_NAME,
    "layers_needed": [
        "heat_density_tot", "nuts_id_number"
    ],
    "type_layer_needed": [
        "heat","nuts_id_number"
    ],
    "vectors_needed": [
    
    ],
    "cm_url": "Do not add something",
    
    "cm_description": """ This module calculates the cost-minimal operation of a 
    portfolio of heat supply technologies in a defined district heating system 
    for each hour of the year. The inputs to the module are hourly profiles for 
    the heat demand in the network, for the potential heat supply from different 
    sources and for energy carrier prices. Furthermore, cost and efficiency parameters 
    for each technology are required. The module yields the costs of heat supply, 
    the share of energy carriers used and the implied CO2 emissions. The module 
    can also be used to optimise the capacities of installed heat supply technologies""",
    "cm_id": CM_ID,
    
    'inputs_calculation_module': INPUTS_CALCULATION_MODULE,
    
    'authorized_scale' : ["NUTS 3", "NUTS 2","NUTS 1", "NUTS 0","Hectare"]
}
