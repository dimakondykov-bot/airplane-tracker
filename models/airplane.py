class Airplane:
    """класс описывает набор характеристик самолёта"""

    __slots__ = [
        'latitude',
        'longitude',
        'altitude',
        'velocity',
        'callsign',
        'country_registration',
    ]

    def __init__(self,
                 country_registration: str,
                 callsign: str,
                 latitude: float,
                 longitude: float,
                 altitude: float,
                 velocity: float,
                 ):

        if (
                not type(latitude) == float
                or not type(longitude) == float
                or not type(altitude) == float
                or not type(velocity) == float
        ):
            raise TypeError('Latitude и longitude mдолжны быть флоат float')

        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.velocity = velocity
        self.callsign = callsign
        self.country_registration = country_registration

    def __eq__(self, other):
        """функция сравнения двух самолётов: Если other не является объектом Airplane — сразу False"""

        if not isinstance(other, Airplane):
            return False
        return self.velocity == other.velocity and self.altitude == other.altitude

    def to_dict(self):
        """Функция преобразует объект Airplane в обычный словарь dict"""
        return {
            'country_registration': self.country_registration,
            'callsign': self.callsign,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'altitude': self.altitude,
            'velocity': self.velocity,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Функция принимает словарь data и создаёт новый объект Airplane"""
        return cls(
            data['country_registration'],
            data['callsign'],
            data['latitude'],
            data['longitude'],
            data['altitude'],
            data['velocity'],
        )
