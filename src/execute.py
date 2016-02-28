from src import occupy
from src import empty
from src import toggle

def execute_cmmds(seats, cmmdslist):
    cmmd = cmmdslist[0]
    x1 =  int(cmmdslist[1])
    y1 = int(cmmdslist[2])
    x2 = int(cmmdslist[4])
    y2 = int(cmmdslist[5])
    if cmmd == 'toggle':
        answer = toggle.toggle_it(x1, y1, x2, y2, seats)
    elif cmmd == 'empty':
        answer = empty.empty_it(x1, y1, x2, y2, seats)
    elif cmmd == 'occupy':
        answer = occupy.occupy_seats(x1, y1, x2, y2, seats)
    else:
        pass
    print(cmmd, x1, y1, x2, y2)
    return answer