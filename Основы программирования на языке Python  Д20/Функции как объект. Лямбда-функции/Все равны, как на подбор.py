def same_by(characteristic, objects):
    return len(set(list(map(characteristic, objects)))) <= 1
