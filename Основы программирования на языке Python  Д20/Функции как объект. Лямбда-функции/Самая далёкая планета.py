def find_farthest_orbit(orb):
    sp = []
    for i in orb:
        if i[0] != i[1]:
            sp.append(i[0] * i[1])
        else:
            sp.append(-1)
    ind = sp.index(max(sp))
    return orb[ind]
