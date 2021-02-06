"""This module contains a collection of functions 
related to floods.

"""


from floodsystem.utils import sorted_by_key
from .station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    """Given a list of stations and tolerance level, returns a list of tuples.
    Tuples contatin station name and latest relative water level and are sorted by relative water level in descending order"""

    Flooded_stations = []
    for i in range(len(stations)):
        relative_level = stations[i].relative_water_level - tol
        if relative_level > 0:
            Flooded_stations += (stations[i], relative_level)
        else:
            pass
        return sorted_by_key(Flooded_stations, 1)
    