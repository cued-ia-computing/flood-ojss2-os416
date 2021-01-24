from .stationdata import build_station_list
from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions, ColumnDataSource, HoverTool
from collections import defaultdict

GM_API_KEY = "AIzaSyAdVSBYQhCPbZIG0fQ-fsNIK4AeQceOJYQ"
stations = build_station_list()

def station_map(stations, zoom=6, map_type='satellite'):
    station_values = defaultdict(list)
    for stat in stations:
        station_values['lon'].append(stat.coord[1])
        station_values['lat'].append(stat.coord[0])
        station_values['name'].append(stat.name)
        station_values['Typical_Range'].append(stat.typical_range)
    source = ColumnDataSource(station_values)
    mid_lat = (max(station_values['lat']) + min(station_values['lat']))/2
    mid_lon = (max(station_values['lon']) + min(station_values['lon']))/2
    hover = HoverTool(
        tooltips = [
            ('Name', '@name'),
            ('Typical Range', '@Typical_Range')
        ]
    )
    gmap_options = GMapOptions(lat=mid_lat, lng=mid_lon, map_type=map_type, zoom=zoom)
    p = gmap(GM_API_KEY, gmap_options, title='River Stations', tools=[hover, 'reset', 'wheel_zoom', 'pan'])
    center = p.circle('lon', 'lat', size=4, alpha=0.2, color='yellow', source=source)
    show(p)