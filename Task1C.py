from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

cam_coords = (52.2053, 0.1218)

stations_within_10km = [i.name for i in stations_within_radius(build_station_list(), cam_coords, 10)]
stations_within_10km.sort()

print(stations_within_10km)