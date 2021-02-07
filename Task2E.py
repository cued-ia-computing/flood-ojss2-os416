from floodsystem.plot import plot_many_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from datetime import timedelta


dt = 10
N = 5

stations = stations_highest_rel_level(build_station_list(), N)
plot_many_water_levels(stations, dt=timedelta(days=dt))
