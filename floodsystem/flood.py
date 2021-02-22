"""This module contains a collection of functions 
related to floods.

"""


from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit, relative_levels
from matplotlib.dates import date2num
import numpy as np
from datetime import timedelta
from collections import defaultdict


def stations_level_over_threshold(stations, tol):
    """Given a list of stations and tolerance level, returns a list of tuples.
    Tuples contatin station name and latest relative water level and are sorted by relative water level in descending order"""

    Flooded_stations = []
    for station in stations:
        rel_level = station.relative_water_level()
        if rel_level == None:
            pass
        elif rel_level > tol:
            Flooded_stations.append((station, rel_level))
        else:
            pass

    return sorted_by_key(Flooded_stations, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    """Given a list of stations, returns N stations at highest risk of flooding"""
    def rel_level(x):
        level = x.relative_water_level()
        if level == None:
            return -69669696969669696969699420
        return level
   
    stations.sort(key=rel_level, reverse=True)
    return stations[:N]

def station_flood_risk(station):
    """Returns the flood risk of a station, can be 'severe', 'high', 'moderate' or 'low'. Returns 'failed' if there is a data error"""

    # Some levels history is not availiable
    try:
        dates, levels = fetch_measure_levels(station.measure_id, timedelta(days=7))
    except:
        return 'failed'
    
    # Checks that levels is a list and typical range is avaliable
    if type(levels) != list or type(dates) != list or len(levels) == 0:
        return 'failed'
    current_rel_level = relative_levels(levels[:1], station)
    if current_rel_level == None:
        return 'failed'
    
    # Checks if current water level is low so polyfit computation can be skipped
    if current_rel_level[0] < 0.5:
        return 'low'
    
    # Converts to relative levels for polyfit
    rel_levels = relative_levels(levels, station)

    # Finds latest gradients of 5th degree polyfit for last 24hrs and 1st degree fit of last week. The gradients at then converted to a number of days until flood if the current gradients are sustained.
    t = date2num(np.array(dates))
    poly1, d01 = polyfit(dates[:int(len(dates)/7)], rel_levels[:int(len(dates)/7)], 5)
    poly2, d02 = polyfit(dates, rel_levels, 1)

    gradient1 = (poly1(t[0] - d01) - poly1(t[1] - d01))/(t[0] - t[1])
    gradient2 = (poly2(t[0] - d02) - poly2(t[1] - d02))/(t[0] - t[1])

    days_to_flood1 = (1 - rel_levels[0]) / gradient1
    days_to_flood2 = (1 - rel_levels[0]) / gradient2

    # Days to flood from each polyfit are averaged and data is used to determine risk level.
    days_to_flood = 0.5*days_to_flood1 + 0.5*days_to_flood2
    
    if rel_levels[0] >= 1:
        return 'severe'
    elif rel_levels[0] >= 0.8 and days_to_flood < 4:
        return 'high'
    elif rel_levels[0] >= 0.5 and days_to_flood < 1:
        return 'moderate'
    else:
        return 'low'


def risk_level(x):
    if x == 'severe':
        return 4
    if x == 'high':
        return 3
    if x == 'moderate':
        return 2
    if x == 'low':
        return 1
    return 0

def stations_at_risk(stations, level):
    """Returns a list of tuples, (station, risk_level) for all stations with risk above level"""

    level = risk_level(level)

    stations = [(i, station_flood_risk(i)) for i in stations]
    return [i for i in stations if risk_level(i[1]) >= level]

def stations_by_risk(stations, level = "low"):
    stations_with_risk = stations_at_risk(stations, level)
    out = defaultdict(list)
    for station, risk in stations_with_risk:
        out[risk].append(station)
    return dict(out)
