from models.airplane import Airplane
from src.info_jets import InfoJets


def test_sort_by_altitude_simple_order():
    airplanes = [
        Airplane("RU", "LOW", 10.0, 20.0, 1000.0, 200.0),
        Airplane("RU", "MID", 11.0, 21.0, 5000.0, 210.0),
        Airplane("RU", "HIGH", 12.0, 22.0, 9000.0, 220.0),
    ]

    result = InfoJets.sort_by_altitude(airplanes)

    altitudes = [plane.altitude for plane in result]
    assert altitudes == [9000.0, 5000.0, 1000.0]

