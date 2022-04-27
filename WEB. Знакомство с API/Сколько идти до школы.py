import sys

from Samples.distance import lonlat_distance
from Samples.geocoder import get_coordinates


def main():
    a1 = sys.argv[1]
    a2 = sys.argv[2]
    a1 = get_coordinates(a1)
    a2 = get_coordinates(a2)
    print(lonlat_distance(a1, a2))


if __name__ == "__main__":
    main()
