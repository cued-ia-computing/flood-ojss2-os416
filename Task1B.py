from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

cam_coords = (52.2053, 0.1218)

x = [(i[0].name, i[0].town, i[1]) for i in stations_by_distance(build_station_list(), cam_coords)]

print("Closest 10:")
print(x[:10])
print("Furthest 10:")
print(x[-10:])