import sys

from Samples.geocoder import get_coordinates, get_nearest_object


def main():
    address = sys.argv[1]
    address_point = get_coordinates(address)
    metro_name = get_nearest_object(address_point, "metro")
    if metro_name:
        print(f"Ближайшее к '{address}' - {metro_name}.")
    else:
        print(f"Рядом с '{address}' - метро нет.")


if __name__ == "__main__":
    main()
