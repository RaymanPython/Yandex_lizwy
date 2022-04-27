from Samples.mapapi_PG import show_map


def main():
    location = "ll=30.097431,59.908131&spn=0.2,0.2"
    route_points = [
        "29.914783,59.891574",
        "30.105881,59.944074",
        "30.237944,59.916487",
        "30.266268,59.919073",
        "30.275489,59.930952",
        "30.310165,59.941203"
    ]
    line = ",".join(route_points)
    line_param = f"pl={line}"
    point = route_points[int(round(len(route_points) / 2))]
    point_param = f"pt={point}"
    show_map(location, "map", add_params="&".join([line_param, point_param]))


if __name__ == "__main__":
    main()
