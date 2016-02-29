def get_cmmds(filename):
    values = []
    next = []
    final = []
    file = open(filename, 'r')
    for line in file:
        values.append(line.split(' '))

    for i in range(len(values)):
        for j in range(4):
            temporary = values[i][j]
            if temporary.endswith('\n'):
                next.append(temporary[:-1])
            else:
                next.append(temporary)

    for i in range(len(next)):
            temporary = next[i]
            if ',' in temporary:
                bridge = temporary.split(',')
                for element in bridge:
                    final.append(element)
            else:
                final.append(temporary)

    sublist = [final[n:n+6] for n in range(0, len(final), 6)]


    return sublist

def execute_cmmds(seats, cmmd, x1, y1, blank, x2, y2):
    if cmmd == toggle:
        seats = toggle.toggle_it(x1, y1, x2, y2, seats)
    elif cmmd == empty:
        seats = empty.empty_it(x1, y1, x2, y2, seats)
    elif cmmd == occupy:
        seats = occupy.occupy_seats(x1, y1, x2, y2, seats)