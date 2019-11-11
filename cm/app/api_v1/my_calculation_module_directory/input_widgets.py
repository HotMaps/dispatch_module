import pandas as pd
import os

path2data = os.path.split(os.path.abspath(__file__))[0]
path_inputs_parameter = os.path.join(path2data,"INPUTS_CALCULATION_MODULE.xlsx")


def load_input_widgets(CM_ID,path=path_inputs_parameter):
    df = pd.read_excel(path).astype(str)
    df["cm_id"] = CM_ID
    out = df.to_dict(orient='records')
    
    for i,data in enumerate(out):
        if data["input_type"] == "select":
            out[i]["input_value"]= data["input_value"].replace("[","").replace("]","").replace("'","").replace('"','').split(",")    
    return out,None


if __name__ == "__main__":
    print('Main: input_widgets.py')
    x,_= load_input_widgets("XX")
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(x)