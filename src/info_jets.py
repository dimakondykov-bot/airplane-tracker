import requests
from models.airplane import Airplane
from src.abstractAPI import BaseAPIClass


class InfoJets(BaseAPIClass):
    """Функция для отслеживания трекера самолётов"""

    def __init__(self, base_url: str = 'https://opensky-network.org/api/states/all') -> None:
        super().__init__(base_url)

    def get_airplanes(self, country_coords: dict[str, float]):
        response = requests.get(self.base_url, params=country_coords)

        if response.ok:
            response_airplanes = response.json()['states']
            airplanes = []
            for airplane_dict in response_airplanes:
                airplane = Airplane(
                    airplane_dict[2],
                    airplane_dict[1],
                    airplane_dict[6],
                    airplane_dict[5],
                    airplane_dict[7],
                    airplane_dict[9],
                )
                airplanes.append(airplane)
            return airplanes

        return None

    @staticmethod
    def get_sorted_airplanes(airplanes: list[Airplane]):
        return sorted(airplanes, key=lambda x: (x.altitude is not None, x.altitude), reverse=True)
