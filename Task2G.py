from floodsystem.plot import plot_many_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_by_risk
from datetime import timedelta


# May take some time to run due to polyfits, station list has been cut for demonstration
stations = build_station_list()[:50]
update_water_levels(stations)
stations_above_high = stations_by_risk(stations, 'high')
for risk in stations_above_high.keys():
    print(risk, ':', [i.name for i in stations_above_high[risk]])

plot_many_water_levels(stations_above_high['severe'], timedelta(days=10), polyfit=5)
