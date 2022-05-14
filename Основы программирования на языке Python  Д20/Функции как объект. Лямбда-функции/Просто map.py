def simple_map(transformation, values):
    a = []
    for i in values:
        a.append(transformation(i))
    return a
