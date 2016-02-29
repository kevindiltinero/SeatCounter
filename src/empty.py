def empty_it(a, b, c, d, nested):
    for i in range(a, c+1):
         for j in range(b, d+1):
             nested[i][j] = 0
    return nested