"""Unit test for the geo module."""

from collections import defaultdict
from floodsystem.geo import rivers_by_station_number, rivers_with_station, stations_by_distance, stations_by_river, stations_within_radius
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


def test_stations_within_radius():

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

    assert stations_within_radius(stations, p, 160) == [stations[0], stations[2]]


def test_rivers_with_station():

    stations = []
    coord_list = [(52.2, 0.11), (53.79648, -1.54785), (50.718395, -1.883377)]
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

    assert rivers_with_station(stations) == {stations[0].river, stations[1].river, stations[2].river}


def test_stations_by_river():

    stations = []
    Riv = defaultdict(list)
    coord_list = [(52.2, 0.11), (53.79648, -1.54785), (50.718395, -1.883377)]
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
        Riv[stations[i].river].append(stations[i])

    assert Riv == (stations_by_river(stations))


def test_rivers_by_station_number():

    stations = []
    coord_list = [(52.2, 0.11), (53.79648, -1.54785), (50.718395, -1.883377)]
    coord_list2 = [(52.7, 0.67), (51.0006, -1.0), (50.718395, -0.9857)]
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
    for i in range(len(coord_list2)):
        # Create a station
        s_id = "test-s-id n"
        m_id = "test-m-id n"
        label = "some station n"
        coord = coord_list2[i]
        trange = (-2.3, 3.4445)
        river = "River" + str(i**2)
        town = "My Town" + str(i)
        stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    assert rivers_by_station_number(stations, 2) == [('River0', 2), ('River1', 2)]
