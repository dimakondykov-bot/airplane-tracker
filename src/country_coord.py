from typing import Any

from src.abstractAPI import BaseAPIClass


class CountryCoord(BaseAPIClass):
    """Функция для получения координат страны"""

    def __init__(self, base_url: str = 'https://nominatim.openstreetmap.org/search'):
        super().__init__(base_url)
        self.format_data = 'json'

    def search_by_address(self, address) -> tuple[dict[str, float], Any] | None:
        """Функция для получения адреса"""

        params = {
            "limit": 1,
            "format": self.format_data,
            "q": address,
            "addressdetails": 1,
            "accept-language": "en"
        }
        headers = {
            "User-Agent": "AirplaneTracker/1.0 (contact: test@mail.ru)",
        }

        response = self.session.get(self.base_url, params=params, headers=headers)

        if response.ok:
            data = response.json()

            if not data:
                return None

            location = data[0]
            geo_coordinates = location.get('boundingbox')
            english_country = location.get('address', {}).get('country')

            return {
                'lamin': float(geo_coordinates[0]),
                'lamax': float(geo_coordinates[1]),
                'lomin': float(geo_coordinates[2]),
                'lomax': float(geo_coordinates[3]),
            }, english_country

        return None
