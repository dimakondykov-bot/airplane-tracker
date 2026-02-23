from src.country_coord import CountryCoord


class DummyResponse:
    def __init__(self, data):
        self._data = data
        self.ok = True

    def json(self):
        return self._data


class DummySession:
    def __init__(self, response):
        self._response = response

    def get(self, url, params=None, headers=None):
        return self._response


def test_search_by_address_happy_path():
    fake_api_response = [
        {
            "boundingbox": ["10.0", "20.0", "30.0", "40.0"],
            "address": {"country": "Testland"},
        }
    ]

    coord = CountryCoord()
    coord.session = DummySession(DummyResponse(fake_api_response))

    result = coord.search_by_address("Testland")

    assert result is not None
    coords, country = result
    assert coords == {
        "lamin": 10.0,
        "lamax": 20.0,
        "lomin": 30.0,
        "lomax": 40.0,
    }
    assert country == "Testland"

