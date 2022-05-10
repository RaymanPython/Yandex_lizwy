def tic_tac_toe(field):
    c = True
    for i in field:
        if len(set(list(i))) == 1 and c:
            print(i[-1], 'win')
            c = False
            break
    for i in range(3):
        if len(set([field[0][i], field[1][i], field[2][i]])) == 1 and c:
            print(field[0][i], 'win')
            c = False
            break
    if c:
        if len(set([field[0][0], field[1][1], field[2][2]])) == 1:
            print(field[0][0], 'win')
            c = False
    if c:
        if len(set([field[0][-1], field[1][-2], field[2][-3]])) == 1:
            print(field[0][-1], 'win')
            c = False
    if c:
        print('draw')
