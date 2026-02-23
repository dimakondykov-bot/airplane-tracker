from models.airplane import Airplane
from src.json_file_handler import JsonFileHandler


def test_save_and_load_roundtrip(tmp_path):
    file_path = tmp_path / "airplanes.json"
    handler = JsonFileHandler(str(file_path))

    airplanes = [
        Airplane("RU", "A1", 10.0, 20.0, 1000.0, 200.0),
        Airplane("RU", "A2", 11.0, 21.0, 2000.0, 250.0),
    ]

    handler.save(airplanes)

    loaded = handler.load([])

    assert len(loaded) == len(airplanes)
    assert [a.to_dict() for a in loaded] == [a.to_dict() for a in airplanes]

