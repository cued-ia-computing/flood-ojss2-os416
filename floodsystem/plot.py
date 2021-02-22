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

def plot_water_levels(station, dates, levels, draw = True, file_name = "levels_plotting.html"):
    """Plots level data and typical range for a station. Returns the Bokeh figure of the plot."""
    df = pd.DataFrame({'date': dates, 'level': levels})
    output_file(file_name)
    min_level = min(station.typical_range[0], min(levels))
    max_level = max(station.typical_range[1], max(levels))
    range = max_level - min_level
    # create a new plot with a datetime axis type
    p = figure(plot_width=800, plot_height=500, x_axis_type="datetime", x_axis_label = "Date", y_range=[min_level - range * 0.1, max_level + range * 0.1], y_axis_label = "Water Level / m", title = station.name)

    p.line(df['date'], df['level'], color='navy', alpha=0.5, legend_label="Level history")
    low_range = Span(location=station.typical_range[0],dimension='width', line_color='green', line_width=2)
    high_range = Span(location=station.typical_range[1],dimension='width', line_color='red', line_width=2)
    p.line([], [], legend_label='Typical Low', line_color="green", line_alpha=1)
    p.line([], [], legend_label='Typical High', line_color="red", line_alpha=1)
    p.renderers.extend([low_range, high_range])
    p.legend.location = "top_left"
    if draw:
        show(p)
    return p

def plot_many_water_levels(stations, dt, polyfit = None, draw = True):
    """Plots level data and typical range for a list of stations with one plot per station. If polyfit = True, the polynomial fit of each station is also added to the plot."""
    
    plots = []
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        if len(levels) != 0:
            if polyfit != None:
                p = plot_water_level_with_fit(station, dates, levels, polyfit, draw = False)
            else:
                p = plot_water_levels(station, dates, levels , draw = False)
            if p != None:
                plots.append(p)
    if draw:
        show(column(plots))
    return plots

def plot_water_level_with_fit(station, dates, levels, p0, draw = True, poly_in = (None, None)):
    """Plots water level data and pth degree polynomial fit for input staion level data."""

    if poly_in == (None, None):
        poly, d0 = polyfit(dates, levels, p0)
    else:
        poly, d0 = poly_in
    p = plot_water_levels(station, dates, levels, draw = False)
    t = date2num(np.array(dates))
    df = pd.DataFrame({'t': dates, 'level': poly(t - d0)})
    p.line(df['t'], df['level'], color='orange', alpha=1, legend_label=str(p0) + "th Degree Polyfit")
    if draw:
        show(p)
    return p