def count_array(a, b, nestedlist):
    count = 0
    for i in range(0, a):
        for j in range(0, b):
            if nestedlist[i][j] == 0:
                count += 1
    return count