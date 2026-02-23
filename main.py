from src.country_coord import CountryCoord
from src.info_jets import InfoJets


def main():
    print("Airplane Tracker")

    while True:
        country = input("Введите название страны: ")

        country_coord_handler = CountryCoord()
        coords, country_en = country_coord_handler.search_by_address(country)

        if coords is not None:
            break

        print("Такой страны не существует или данных по стране нет")

    jets_handler = InfoJets()
    airplanes = jets_handler.get_airplanes(coords)

    airplane_by_country_registration = []

    for airplane in airplanes:
        if airplane.country_registration == country_en:
            airplane_by_country_registration.append(airplane)

    airplanes = jets_handler.get_sorted_airplanes(airplane_by_country_registration)

    while True:
        n = input("Введите max самолётов в ответе: ")

        try:
            n = int(n)
            if 0 < n > len(airplanes):
                break
            print(f"Число вне диапазона: {len(airplanes)}")
        except ValueError:
            print("Не число")

    for airplane in airplanes[:n]:
        print(airplane.to_dict())


if __name__ == '__main__':
    main()
