def occupy_seats(a, b, c, d, nestedlist):
    for i in range(a, c+1):
         for j in range(b, d+1):
             nestedlist[i][j] = 1
    return nestedlist