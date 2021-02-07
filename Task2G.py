from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from datetime import timedelta
from bokeh.plotting import show
from bokeh.models import Span

dt = 10
i = 16
stations = build_station_list()
dates, levels = fetch_measure_levels(stations[i].measure_id, dt=timedelta(days=dt))
x = int(len(dates) * 0.2)
poly, d0 = polyfit(dates[x:], levels[x:], 3)

p = plot_water_level_with_fit(stations[i], dates, levels, 10, draw=False, poly_in=(poly, d0))
print(dates[x])
end = Span(location=dates[x], dimension='height', line_color='blue', line_width=2)

p.renderers.extend([end])
show(p)
