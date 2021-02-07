from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


stations = build_station_list()
update_water_levels(stations)

stations_over_threshold = stations_level_over_threshold(stations, 0.8)

for i in stations_over_threshold:
    print(i[0].name, i[1])
