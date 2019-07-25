import pandas as pd
import os

path2data = os.path.split(os.path.abspath(__file__))[0]
path_inputs_parameter = os.path.join(path2data,"INPUTS_CALCULATION_MODULE.xlsx")


def load_input_widgets(CM_ID,path=path_inputs_parameter):
    df = pd.read_excel(path)
    df["cm_id"] = CM_ID
    return df.to_dict(orient='records'),None 



if __name__ == "__main__":
    print('Main: input_widgets.py')