from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from datetime import datetime, timedelta



dt = 10
N = 5

stations = stations_highest_rel_level(build_station_list(), N):
for station in stations:
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
    plot_water_levels(station, dates, levels)