from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

stations = build_station_list()
rivers = list(rivers_with_station(stations))
rivers.sort()

print(len(rivers))
print(rivers[:10])

test_rivers = ('River Aire', 'River Cam', 'River Thames')
river_stations = stations_by_river(stations)

for river in test_rivers:
    station_list = [i.name for i in river_stations[river]]
    station_list.sort()
    print(station_list)
