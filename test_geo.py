"""Unit test for the geo module."""

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation


def test_stations_by_distance():

    stations = []
    coord_list = [(52.2, 0.11), (53.79648, -1.54785), (50.718395, -1.883377)]
    p = (51.509865, -0.118092)
    for i in range(len(coord_list)):
        # Create a station
        s_id = "test-s-id n"
        m_id = "test-m-id n"
        label = "some station n"
        coord = coord_list[i]
        trange = (-2.3, 3.4445)
        river = "River" + str(i)
        town = "My Town" + str(i)
        stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    assert stations_by_distance(stations, p) == [(stations[0], 78.32212827453219),
                                                 (stations[2], 151.419460832818),
                                                 (stations[1], 271.9227491652322)]
