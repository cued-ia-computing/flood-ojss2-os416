"""This module contains a collection of functions related to
plotting data.

"""

from .datafetcher import fetch_measure_levels
from .analysis import polyfit
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import Span
import pandas as pd
import numpy as np
from matplotlib.dates import date2num

def plot_water_level(station, dates, levels, draw = True):
    df = pd.DataFrame({'date': dates, 'level': levels})
    output_file("datetime.html")
    min_level, max_level = station.typical_range
    range = max_level - min_level
    # create a new plot with a datetime axis type
    p = figure(plot_width=800, plot_height=500, x_axis_type="datetime", y_range=[min_level - range * 0.1, max_level + range * 0.1])

    p.line(df['date'], df['level'], color='navy', alpha=0.5)
    low_range = Span(location=min_level,dimension='width', line_color='green',line_width=2)
    high_range = Span(location=max_level,dimension='width', line_color='red',line_width=2)
    p.renderers.extend([low_range, high_range])
    if draw:
        show(p)
    return p

def plot_many_water_levels(stations, dt, polyfit = None):
    plots = []
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        if polyfit != None:
            p = plot_water_level_with_fit(station, dates, levels, polyfit, draw = False)
        else:
            p = plot_water_level(station, dates, levels , draw = False)
        plots.append(p)
    show(column(plots))

def plot_water_level_with_fit(station, dates, levels, p, draw = True, poly_in = (None, None)):
    if poly_in == (None, None):
        poly, d0 = polyfit(dates, levels, p)
    else:
        poly, d0 = poly_in[0], poly_in[1]
    p = plot_water_level(station, dates, levels, draw = False)
    t = date2num(np.array(dates))
    df = pd.DataFrame({'t': dates, 'level': poly(t - d0)})
    p.line(df['t'], df['level'], color='orange', alpha=1)
    if draw:
        show(p)
    return p