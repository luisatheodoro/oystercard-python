import mock


def victoria_station():
    m = mock.Mock()
    m.victoria_station = 'victoria station'
    return m.victoria_station


def aldgate_station():
    m = mock.Mock()
    m.aldgate_station = 'aldgate station'
    return m.aldgate_station


def journey():
    m = mock.Mock()
    m.journey = {1: {"entry_station": "victoria station", "exit_station": "aldgate station"}}
    return m.journey
