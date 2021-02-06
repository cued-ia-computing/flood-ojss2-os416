"""This module contains a collection of functions 
related to floods.

"""


from floodsystem.utils import sorted_by_key
from .station import MonitoringStation


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
 


    