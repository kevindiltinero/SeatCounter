def toggle_it(a, b, c, d, nestedlist):
    for i in range(a, c+1):
        for j in range(b, d+1):
            if nestedlist[i][j] == 1:
                nestedlist[i][j] = 0
            elif nestedlist[i][j] == 0:
                nestedlist[i][j] = 1
            else:
                pass
    return nestedlist

