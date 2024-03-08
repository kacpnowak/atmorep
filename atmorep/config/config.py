import os 
from pathlib import Path

fpath = os.path.dirname(os.path.realpath(__file__))

year_base = 2011
year_last = 2020

path_models = Path( fpath, '../../models/')
path_results = Path( fpath, '../../results/')
path_data = Path( fpath, '../../../data/one-degree/')
path_plots = Path( fpath, '../results/plots/')
fname_base = '{}/{}/{}.{}.{}'

filler_value = 0.0
months_per_file = 12
spatial_resolution = 1 # Degree
# 1/Spatial resolution for data. Eg. for 1 deg -> 1, for 0.25 deg -> 4
number_of_steps_per_degree = 1
# Number of mesh elements
lat_range = 170
long_range = 360


grib_index = { 'vorticity' : 'vo', 'divergence' : 'd', 'geopotential' : 'z',
                'orography' : 'z', 'temperature': 'temp', 'specific_humidity' : 'q',
                'mean_top_net_long_wave_radiation_flux' : 'mtnlwrf',
                'velocity_u' : 'u', 'velocity_v': 'v', 'velocity_z' : 'w',
                'total_precip' : 'tp', 'radar_precip' : 'yw_hourly',
                't2m' : 't_2m', 'u_10m' : 'u_10m', 'v_10m' : 'v_10m',
                'salinity': 'salt'}
