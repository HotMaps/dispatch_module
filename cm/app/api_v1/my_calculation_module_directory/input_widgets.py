import pandas as pd, numpy as np
import os
import pprint

path2data = os.path.join(os.path.split(os.path.abspath(__file__))[0],"input_data")
path_inputs_parameter = os.path.join(path2data,"INPUTS_CALCULATION_MODULE.xlsx")
path_inputs_output=os.path.join(path2data,"INPUTS_CALCULATION_MODULE.txt")

def load_input_widgets(CM_ID="CM_ID",path=path_inputs_parameter,outpath=path_inputs_output): 
    df = pd.read_excel(path).replace(np.nan, '', regex=True).astype(str)
    df["input_type"] = df.input_type.str.strip()
    df["cm_id"] = CM_ID 
    out = df.to_dict(orient='records') 
     
    for i,data in enumerate(out): 
        if data["input_type"] == "select": 
            out[i]["input_value"] = [x.strip() for x in data["input_value"].replace("[","").replace("]","").replace("'","").replace('"','').split(",")]   
        
    with open(outpath,"w") as fp:
        pprint.pprint(out,fp)
    #    return out
    
    with open(outpath,"r") as fp:
        data = fp.read()
    data=data.replace(f"'{CM_ID}'",f'{CM_ID}')
    with open(outpath,"w") as fp:
        fp.write(data)        
    return data

if __name__ == "__main__":
    print('Main: input_widgets.py')
    out = load_input_widgets()