import random

from Samples.geocoder import get_ll_span
from Samples.mapapi_PG import show_map


def main():
    towns = [
        "Ярославль",
        "Нижний Новгород",
        "Казань",
        "Великий Новгород",
        "Архангельск",
        "Саратов",
        "Петрозаводск",
        "Астрахань"
    ]
    random.shuffle(towns)

    for town in towns:
        ll, spn = get_ll_span(town)
        map_type = "sat"
        if random.random() > 0.5:
            spn = "0.001,0.001"
            map_type = "map"
        ll_spn = f"ll={ll}&spn={spn}"
        show_map(ll_spn, map_type)


if __name__ == "__main__":
    main()
