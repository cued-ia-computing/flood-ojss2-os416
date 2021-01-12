from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

x = [i.name for i in inconsistent_typical_range_stations(build_station_list())]
x.sort()

print(x)
