from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold


def test_stations_level_over_threshold():

    stations = []
    trange_list = [(0.5, 2.5), (-1, 6), (2, 1)]
    p = (51.509865, -0.118092)
    for i in range(len(trange_list)):
        # Create a station
        s_id = "test-s-id n"
        m_id = "test-m-id n"
        label = "some station n"
        coord = (52, 1)
        trange = trange_list[i]
        river = "River" + str(i)
        town = "My Town" + str(i)
        stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    stations[0].latest_level = 1.5
    stations[1].latest_level = 4
    stations[2].latest_level = 2
    
    assert stations_level_over_threshold(stations, 0.6) == [(stations[1], 0.7142857142857143)]

def test_stations_highest_rel_water_level():
    stations = []
    trange_list = [(0.5, 2.5), (-1, 6), (-3, 1)]
    p = (51.509865, -0.118092)
    for i in range(len(trange_list)):
        # Create a station
        s_id = "test-s-id n"
        m_id = "test-m-id n"
        label = "some station n"
        coord = (52, 1)
        trange = trange_list[i]
        river = "River" + str(i)
        town = "My Town" + str(i)
        stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))
    stations[0].latest_level = 1.5 
    stations[1].latest_level = 2   
    stations[2].latest_level = 2   
    high_level = [stations[2], stations[0]]

    assert stations_highest_rel_level(stations, 2) == high_level
