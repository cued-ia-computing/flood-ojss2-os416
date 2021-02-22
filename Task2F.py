from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_many_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from datetime import timedelta

dt = 2
N = 5
p0 = 4

stations = build_station_list()
update_water_levels(stations)
stations = stations_highest_rel_level(stations, N)
plot_many_water_levels(stations, dt=timedelta(days=dt), polyfit=p0)
