from floodsystem.plot import plot_many_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from datetime import timedelta


dt = 10
N = 5

stations = build_station_list()
update_water_levels(stations)
stations = stations_highest_rel_level(stations, N)
plot_many_water_levels(stations, dt=timedelta(days=dt))
