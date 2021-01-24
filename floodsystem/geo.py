# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from collections import defaultdict

def stations_by_distance(stations, p):
    """Test"""
    station_list = []
    for station in stations:
        station_list.append((station, haversine(station.coord, p)))
    
    return sorted_by_key(station_list, 1)

def stations_within_radius(stations, centre, r):
    """Test 2"""
    station_list = [i for i in stations if haversine(i.coord, centre) <= r]

    return station_list

def rivers_with_station(stations):
    return {i.river for i in stations}

def stations_by_river(stations):
    station_river = defaultdict(list)
    for i in stations:
        station_river[i.river].append(i)

    return station_river

def rivers_by_station_number(stations, N):
    stations_per_river = [(river, len(stats)) for river, stats in stations_by_river(stations).items()]
    stations_per_river = sorted_by_key(stations_per_river, 1, True)
    min_stations = stations_per_river[N-1][1]
    cut_list = stations_per_river[:N]
    i = N
    while stations_per_river[i][1] == min_stations:
        cut_list.append(stations_per_river[i])
        i+=1
    return cut_list
    