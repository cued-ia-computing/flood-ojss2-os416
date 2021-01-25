"""Unit test for the geo module."""

import floodsystem.geo

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from collections import defaultdict
from stationdata import build_station_list

def test_stations_by_distance():

    stations = []
    n = 0

    for n in range 3:
                    # Create a station
        s_id = "test-s-id n"
        m_id = "test-m-id n"
        label = "some station n"
        coord = (-2.0*n, 4.0)
        trange = (-2.3*n, 3.4445)
        river = "River" + str(n)
        town = "My Town" + str(n)
        stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    return stations

print(test_stations_by_distance())


    

