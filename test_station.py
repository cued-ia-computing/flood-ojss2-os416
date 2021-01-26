# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consitent():

    # Create a station
    s_id = "test-s-id n"
    m_id = "test-m-id n"
    label = "some station n"
    coord = (53.645, -0.83453)
    trange = (5.3, 3.4445)
    river = "River"
    town = "My Town"
    station = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert station.typical_range_consistent == False


def test_inconsistent_typical_range_stations():

    stations = []
    coord_list = [(52.2, 0.11), (53.79648, -1.54785), (50.718395, -1.883377)]
    # Create a station
    for i in range(len(coord_list)):
        s_id = "test-s-id n"
        m_id = "test-m-id n"
        label = "some station n"
        coord = coord_list[i]
        trange = (-5.3 + (4 * i), 2)
        river = "River" + str(i)
        town = "My Town" + str(i)
        stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    assert inconsistent_typical_range_stations(stations) == [stations[2]]
