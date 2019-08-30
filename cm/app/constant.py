
CELERY_BROKER_URL_DOCKER = 'amqp://admin:mypass@rabbit:5672/'
CELERY_BROKER_URL_LOCAL = 'amqp://localhost/'


CM_REGISTER_Q = 'rpc_queue_CM_register' # Do no change this value

CM_NAME = 'CM - District heating supply dispatch'
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

INPUTS_CALCULATION_MODULE = [   {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'Heat Boiler - Thermal Output Capacity',
        'input_parameter_name': 'hb_cap',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'MW',
        'input_value': '10'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'Heat Pump - Thermal Output Capacity ',
        'input_parameter_name': 'hp_cap',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'MW',
        'input_value': '20'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'Solar Thermal - Thermal Output Capacity ',
        'input_parameter_name': 'st_cap',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'MW',
        'input_value': '30'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'Back Pressure CHP - Thermal Output Capacity ',
        'input_parameter_name': 'chp_cap',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'MW',
        'input_value': '40'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'Waste Incineration Plant - Thermal Output Capacity',
        'input_parameter_name': 'wi_cap',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'MW',
        'input_value': '50'},
    {   'cm_id': CM_ID,
        'input_max': '1',
        'input_min': '0.001',
        'input_name': 'Heat Boiler - thermal efficiency ',
        'input_parameter_name': 'hb_nth',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'none',
        'input_value': '0.875'},
    {   'cm_id': CM_ID,
        'input_max': '1',
        'input_min': '0.001',
        'input_name': 'Heat Pump  - thermal efficiency',
        'input_parameter_name': 'hp_nth',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'none',
        'input_value': '3'},
    {   'cm_id': CM_ID,
        'input_max': '1',
        'input_min': '0.001',
        'input_name': 'Solar Thermal - thermal efficiency',
        'input_parameter_name': 'st_nth',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'none',
        'input_value': '1'},
    {   'cm_id': CM_ID,
        'input_max': '1',
        'input_min': '0.001',
        'input_name': 'Back Pressure CHP - thermal efficiency',
        'input_parameter_name': 'chp_nth',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'none',
        'input_value': '0.36'},
    {   'cm_id': CM_ID,
        'input_max': '1',
        'input_min': '0.001',
        'input_name': 'Waste Incineration Plant- thermal efficiency ',
        'input_parameter_name': 'wi_nth',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'none',
        'input_value': '0.36'},
    {   'cm_id': CM_ID,
        'input_max': '1',
        'input_min': '0.001',
        'input_name': 'Heat Boiler - electrical efficiency ',
        'input_parameter_name': 'hb_nel',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'none',
        'input_value': '0'},
    {   'cm_id': CM_ID,
        'input_max': '1',
        'input_min': '0.001',
        'input_name': 'Heat Pump  - electrical efficiency ',
        'input_parameter_name': 'hp_nel',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'none',
        'input_value': '0'},
    {   'cm_id': CM_ID,
        'input_max': '1',
        'input_min': '0.001',
        'input_name': 'Solar Thermal - electrical efficiency',
        'input_parameter_name': 'st_nel',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'none',
        'input_value': '0'},
    {   'cm_id': CM_ID,
        'input_max': '1',
        'input_min': '0.001',
        'input_name': 'Back Pressure CHP - electrical efficiency ',
        'input_parameter_name': 'chp_nel',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'none',
        'input_value': '0.5'},
    {   'cm_id': CM_ID,
        'input_max': '1',
        'input_min': '0.001',
        'input_name': 'Waste Incineration Plant- electrical efficiency ',
        'input_parameter_name': 'wi_nel',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'none',
        'input_value': '0.45'},
    {   'cm_id': CM_ID,
        'input_max': 'none',
        'input_min': 'none',
        'input_name': 'Heat Boiler - energy carrier ',
        'input_parameter_name': 'hb_ec',
        'input_priority': '1',
        'input_type': 'select',
        'input_unit': 'EUR/MWh',
        'input_value': [   'electricity',
                           ' bio gas',
                           ' waste',
                           ' wood pellets',
                           ' radiation',
                           ' various']},
    {   'cm_id': CM_ID,
        'input_max': 'none',
        'input_min': 'none',
        'input_name': 'Heat Pump  - Capacity ',
        'input_parameter_name': 'hp_ec',
        'input_priority': '0',
        'input_type': 'select',
        'input_unit': 'EUR/MWh',
        'input_value': [   'electricity',
                           ' bio gas',
                           ' waste',
                           ' wood pellets',
                           ' radiation',
                           ' various']},
    {   'cm_id': CM_ID,
        'input_max': 'none',
        'input_min': 'none',
        'input_name': 'Solar Thermal - Capacity ',
        'input_parameter_name': 'st_ec',
        'input_priority': '4',
        'input_type': 'select',
        'input_unit': 'EUR/MWh',
        'input_value': [   'electricity',
                           ' bio gas',
                           ' waste',
                           ' wood pellets',
                           ' radiation',
                           ' various']},
    {   'cm_id': CM_ID,
        'input_max': 'none',
        'input_min': 'none',
        'input_name': 'Back Pressure CHP - Capacity ',
        'input_parameter_name': 'chp_ec',
        'input_priority': '3',
        'input_type': 'select',
        'input_unit': 'EUR/MWh',
        'input_value': [   'electricity',
                           ' bio gas',
                           ' waste',
                           ' wood pellets',
                           ' radiation',
                           ' various']},
    {   'cm_id': CM_ID,
        'input_max': 'none',
        'input_min': 'none',
        'input_name': 'Waste Incineration Plant- Capacity ',
        'input_parameter_name': 'wi_ec',
        'input_priority': '2',
        'input_type': 'select',
        'input_unit': 'EUR/MWh',
        'input_value': [   'electricity',
                           ' bio gas',
                           ' waste',
                           ' wood pellets',
                           ' radiation',
                           ' various']},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Heat Boiler - OPEX fix ',
        'input_parameter_name': 'hb_opexFix',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MW',
        'input_value': '9000'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Heat Pump  - OPEX fix ',
        'input_parameter_name': 'hp_opexFix',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MW',
        'input_value': '10000'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Solar Thermal - OPEX fix ',
        'input_parameter_name': 'st_opexFix',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MW',
        'input_value': '10000'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Back Pressure CHP - OPEX fix ',
        'input_parameter_name': 'chp_opexFix',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MW',
        'input_value': '34000'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Waste Incineration Plant- OPEX fix',
        'input_parameter_name': 'wi_opexFix',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MW',
        'input_value': '100000'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Heat Boiler - OPEX var ',
        'input_parameter_name': 'hb_opexVar',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MWh',
        'input_value': '1.5'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Heat Pump  - OPEX var ',
        'input_parameter_name': 'hp_opexVar',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MWh',
        'input_value': '0.5'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Solar Thermal - OPEX var ',
        'input_parameter_name': 'st_opexVar',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MWh',
        'input_value': '0.5'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Back Pressure CHP - OPEX var ',
        'input_parameter_name': 'chp_opexVar',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MWh',
        'input_value': '4.5'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Waste Incineration Plant- OPEX var ',
        'input_parameter_name': 'wi_opexVar',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MWh',
        'input_value': '0.5'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Heat Boiler - investment cost ',
        'input_parameter_name': 'hb_ic',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MW',
        'input_value': '474000'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Heat Pump  - investment cost ',
        'input_parameter_name': 'hp_ic',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MW',
        'input_value': '510000'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Solar Thermal - investment cost ',
        'input_parameter_name': 'st_ic',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MW',
        'input_value': '550000'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Back Pressure CHP - investment cost ',
        'input_parameter_name': 'chp_ic',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MW',
        'input_value': '1300000'},
    {   'cm_id': CM_ID,
        'input_max': '10000000',
        'input_min': '0',
        'input_name': 'Waste Incineration Plant- investment cost ',
        'input_parameter_name': 'wi_ic',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MW',
        'input_value': '1200000'},
    {   'cm_id': CM_ID,
        'input_max': '50',
        'input_min': '0',
        'input_name': 'Heat Boiler - lifetime ',
        'input_parameter_name': 'hb_lt',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'a',
        'input_value': '21'},
    {   'cm_id': CM_ID,
        'input_max': '50',
        'input_min': '0',
        'input_name': 'Heat Pump  -  lifetime',
        'input_parameter_name': 'hp_lt',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'a',
        'input_value': '25'},
    {   'cm_id': CM_ID,
        'input_max': '50',
        'input_min': '0',
        'input_name': 'Solar Thermal -  lifetime ',
        'input_parameter_name': 'st_lt',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'a',
        'input_value': '20'},
    {   'cm_id': CM_ID,
        'input_max': '50',
        'input_min': '0',
        'input_name': 'Back Pressure CHP -  lifetime',
        'input_parameter_name': 'chp_lt',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'a',
        'input_value': '25'},
    {   'cm_id': CM_ID,
        'input_max': '50',
        'input_min': '0',
        'input_name': 'Waste Incineration Plant-  lifetime ',
        'input_parameter_name': 'wi_lt',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'a',
        'input_value': '20'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'energy carrier price - electricity ',
        'input_parameter_name': 'electricity_p',
        'input_priority': '1',
        'input_type': 'input',
        'input_unit': 'EUR/MWh',
        'input_value': '0'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'energy carrier price - Bio Gas ',
        'input_parameter_name': 'bio gas_p',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MWh',
        'input_value': '100'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'energy carrier price - waste ',
        'input_parameter_name': 'waste_p',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MWh',
        'input_value': '1'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'energy carrier price - wood pellets ',
        'input_parameter_name': 'wood pellets_p',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MWh',
        'input_value': '36'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'energy carrier price - radiation ',
        'input_parameter_name': 'radiation_p',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MWh',
        'input_value': '0'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'energy carrier price - various ',
        'input_parameter_name': 'various_p',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/MWh',
        'input_value': '22'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'emission factor - electricity ',
        'input_parameter_name': 'electricity_ef',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'tCO2/MWh',
        'input_value': '0.8'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'emission factor - gas. Biomass ',
        'input_parameter_name': 'bio gas_ef',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'tCO2/MWh',
        'input_value': '0'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'emission factor  - waste ',
        'input_parameter_name': 'waste_ef',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'tCO2/MWh',
        'input_value': '0.05'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'emission factor  - wood pellets ',
        'input_parameter_name': 'wood pellets_ef',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'tCO2/MWh',
        'input_value': '0'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'emission factor  - radiation ',
        'input_parameter_name': 'radiation_ef',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'tCO2/MWh',
        'input_value': '0'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'emission factor  - various ',
        'input_parameter_name': 'various_ef',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'tCO2/MWh',
        'input_value': '0'},
    {   'cm_id': CM_ID,
        'input_max': '100000',
        'input_min': '0',
        'input_name': 'CO2 Price ',
        'input_parameter_name': 'pCO2_pCO2',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'EUR/tCO2',
        'input_value': '25'},
    {   'cm_id': CM_ID,
        'input_max': 'none',
        'input_min': 'none',
        'input_name': 'interest rate ',
        'input_parameter_name': 'ir_ir',
        'input_priority': '0',
        'input_type': 'input',
        'input_unit': 'none',
        'input_value': '0.05'},
    {   'cm_id': CM_ID,
        'input_max': 'none',
        'input_min': 'none',
        'input_name': 'invest mode',
        'input_parameter_name': 'if_if',
        'input_priority': '0',
        'input_type': 'select',
        'input_unit': 'none',
        'input_value': ['invest', 'dispatch']}]




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
