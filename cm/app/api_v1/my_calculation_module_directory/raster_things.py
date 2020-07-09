import os,sys
from osgeo import gdal
import numpy as np, pandas as pd
from .mydecorator import decore_message
import geopandas as gpd
from shapely.geometry import Point
import pickle
import numpy as np

path2data = path2data = os.path.join(os.path.split(os.path.abspath(__file__))[0],"input_data")
path_nuts_code = os.path.join(path2data,"data_nuts_id_number.csv")

@decore_message
def load_profile(nuts0,profile_name="radiation_profiles.dat"):
    with open(os.path.join(path2data,profile_name),"rb") as file:
        dat = pickle.load(file)
        try:
            val = dat[(nuts0, '2008-2016')].tolist()
        except:
            print("#"*100)
            print("Warning use AT as profile")
            print("#"*100)
            val = dat[("AT", '2008-2016')].tolist() 
    return val,None

@decore_message
def get_nuts(nuts_code):
    nuts3 = nuts_code[:5]
    nuts2 = nuts_code[:4]
    nuts1 = nuts_code[:3]
    nuts0 = nuts_code[:2]
    return (nuts3,nuts2,nuts1,nuts0),None  

@decore_message
def raster_array(raster, dType=float, return_gt=False):
    ds = gdal.Open(raster)
    geo_transform = ds.GetGeoTransform()
    band1 = ds.GetRasterBand(1)
    arr = band1.ReadAsArray().astype(dType)
    ds = None
    if return_gt:
        return (arr, geo_transform),None  # 0..x,1...xres,3..y,5...yres
    else:
        return arr,None
    
@decore_message
def return_nuts_codes(path_to_raster):
    code_list = pd.read_csv(path_nuts_code)
    code_list = code_list.set_index("id")["nuts_code"]
    arr,message = raster_array(path_to_raster)
    arr = arr.astype(int)
    unique_val, counts = np.unique(arr[arr!=0] ,return_counts=True)
    # In case of region selection from several NUTS 3 areas, only the one with
    # highest number of elements is selected.
    code = unique_val[counts.argmax()]
    nuts_code = code_list[int(code)]
    (nuts3,nuts2,nuts1,nuts0),message = get_nuts(nuts_code)
    return (nuts0, nuts1, nuts2, nuts3),message   


@decore_message
def get_temperature_and_radiation(point,nuts0,target_epsg=4326,init_epsg=3035):
    os.environ['PROJ_LIB']  = os.path.join(os.path.dirname(sys.executable),"Library","share")
    p = gpd.GeoDataFrame([[Point(point)]], geometry='geometry', crs={'init': f'epsg:{init_epsg}'}, columns=['geometry'])   
    p = p.to_crs(epsg=target_epsg)
    lon = float(p.geometry.x)
    lat = float(p.geometry.y)
#    https://re.jrc.ec.europa.eu/pvg_static/web_service.html#HR
    try:
        req = f"https://re.jrc.ec.europa.eu/api/tmy?lat={lat}&lon={lon}"
        df = pd.read_csv(req,sep=",",skiprows=list(range(16))+list(range(8777,8790)))
        rad = df["G(h)"].values.tolist()
        temp = df["T2m"].values.tolist()
    except:
        print("#"*100)
        print("Server https://re.jrc.ec.europa.eu/ not working using local data")
        print("#"*100)
        rad,_ = load_profile(nuts0,"radiation_profiles.dat")
        temp,_ = load_profile(nuts0,"temperature_profiles.dat")

    radiation = dict(zip(range(1,8760+1),rad))
    temperature = dict(zip(range(1,8760+1),temp))
    out = dict(temperature_t=temperature,radiation_t=radiation)
    return out,None


@decore_message
def get_max_heat_point(path_to_raster):
    out,message = raster_array(path_to_raster,return_gt=True)
    if out == -1:
        return out,message
    (arr,(x0,dx,_,y0,__,dy)) = out
    kx,ky = np.unravel_index(arr.argmax(), arr.shape)
    x = x0 + kx*dx
    y = y0 + ky*dy
    return (x,y),message    


    

     
