#from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_many_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta

dt = 2
N = 5
p = 4

#stations = stations_highest_rel_level(build_station_list()[6], N)
stations = build_station_list()[6:8]

plot_many_water_levels(stations, dt=timedelta(days=dt), polyfit = p)