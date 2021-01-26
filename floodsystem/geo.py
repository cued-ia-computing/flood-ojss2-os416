# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine
from collections import defaultdict

def stations_by_distance(stations, p):
    """Given a list of stations and a coordinate (p), returns a list of tuples - (station, distance from p) ordered by distance"""
    station_list = []
    for station in stations:
        station_list.append((station, haversine(station.coord, p)))
    
    return sorted_by_key(station_list, 1)

def stations_within_radius(stations, centre, r):
    """Given a list of stations and a circle with a radius r and centre point defined by co-ordinates, returns a list of stations within the circle"""
    station_list = [i for i in stations if haversine(i.coord, centre) <= r]

    return station_list

def rivers_with_station(stations):
    """Given a list of stations, returns a list of corresponding rivers"""
    return {i.river for i in stations}

def stations_by_river(stations):
    """Given a list of stations, creates a dictionary of the stations with corresponding rivers as the key"""
    station_river = defaultdict(list)
    for i in stations:
        station_river[i.river].append(i)

    return station_river

def rivers_by_station_number(stations, N):
    """Given a list of stations, returns a list of N many rivers and the number of stations on them, in decending order"""
    stations_per_river = [(river, len(stats)) for river, stats in stations_by_river(stations).items()]
    stations_per_river = sorted_by_key(stations_per_river, 1, True)
    min_stations = stations_per_river[N-1][1]
    cut_list = stations_per_river[:N]
    i = N
    while stations_per_river[i][1] == min_stations:
        cut_list.append(stations_per_river[i])
        i+=1
    return cut_list
    