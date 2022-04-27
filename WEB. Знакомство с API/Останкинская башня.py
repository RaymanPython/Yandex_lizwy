import sys
from Samples.distance import lonlat_distance
from Samples.geocoder import get_coordinates


def calc_antenna_height(distance, transmitter_height):
    x = distance / 3.6 - (transmitter_height ** 0.5)
    return x * x if x > 0 else 0


def main():
    ostankino_address = "Москва, улица Академика Королёва, 15к1"
    ostankino_height = 525
    address = sys.argv[1]
    ostankino_point = get_coordinates(ostankino_address)
    address_point = get_coordinates(address)
    distance = math.trunc(lonlat_distance(ostankino_point, address_point) / 1000)
    antenna_height = round(calc_antenna_height(distance, ostankino_height))
    print(f"Высота антенны на расстоянии {distance} км. составляет {antenna_height} м.")


if __name__ == "__main__":
    main()
