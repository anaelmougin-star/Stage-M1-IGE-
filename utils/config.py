0# /home/mougina/mes_analyses_neige/config.py

import scipy.ndimage as ndi
import numpy as np
import xarray as xr

ds_grid = xr.open_dataset("/bettik/castelli/data/MAR-ERA5/MAR3.14/EUo/MARgrid_EUo.nc")

lon = np.array(ds_grid.LON)
lat = np.array(ds_grid.LAT)
H = np.array(ds_grid.SH)

def detect_alps(H):
    nlat, nlon = np.shape(H)
    mask = np.bool_(np.zeros((nlat, nlon)))
    r = 4
    for j in range(r, nlat-r):
        for i in range(r, nlon-r):
            mask[j,i] = np.logical_and(H[j,i]>360, np.any(H[j-r:j+r, i-r:i+r]>1300))
    return mask


alps = detect_alps(H)
alps[lon<4.8] = False
alps[np.logical_and(lon>10, lat<45.2)] = False
alps = ndi.binary_fill_holes(alps)

def detect_alps_with_ice_mask(H):
    nlat, nlon = np.shape(H)
    mask = np.bool_(np.zeros((nlat, nlon)))
    r = 4
    for j in range(r, nlat-r):
        for i in range(r, nlon-r):
            mask[j,i] = np.logical_and(H[j,i]>360, np.any(H[j-r:j+r, i-r:i+r]>1300))
    return mask

alps_ice = detect_alps_with_ice_mask(H)
alps_ice[lon<4.8] = False
alps_ice[np.logical_and(lon>10, lat<45.2)] = False
alps_ice = ndi.binary_fill_holes(alps_ice)

# Masque glacier depuis V4
ds_v4_ref = xr.open_dataset("/bettik/PROJECTS/pr-regional-climate/mougina/data_v4_GF_alps/SCFG_Alps_2018.nc", decode_cf=False)
for v in ds_v4_ref.variables:
    if 'dtype' in ds_v4_ref[v].attrs:
        del ds_v4_ref[v].attrs['dtype']
ds_v4_ref = xr.decode_cf(ds_v4_ref)
is_ice = (ds_v4_ref['scfg'] == 215).any(dim='time').astype(float)  
is_ice_regrid = is_ice.interp(lon=ds_grid.LON, lat=ds_grid.LAT, method="nearest").astype(bool)
alps_ice[is_ice_regrid.values] = False



#fonction saison

def get_season(t):
    if t.month in [12, 1, 2]:
        return f"{t.year + 1}_DJF" if t.month == 12 else f"{t.year}_DJF"
    elif t.month in [3, 4, 5]:
        return f"{t.year}_MAM"
    elif t.month in [6, 7, 8]:
        return f"{t.year}_JJA"
    elif t.month in [9, 10, 11]:
        return f"{t.year}_SON"