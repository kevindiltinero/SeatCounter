from src import create
from src import occupy
from src import count
from src import empty
from src import toggle
from src import thefile

def execute_cmmds(seats, cmmdslist):
    reseats = []
    cmmd = cmmdslist[0]
    x1 =  cmmdslist[1]
    y1 = cmmdslist[2]
    x2 = cmmdslist[4]
    y2 = cmmdslist[5]
    if cmmd == toggle:
        reseats.append(toggle.toggle_it(x1, y1, x2, y2, seats))
    elif cmmd == empty:
        reseats.append(empty.empty_it(x1, y1, x2, y2, seats))
    elif cmmd == occupy:
        reseats.append(occupy.occupy_seats(x1, y1, x2, y2, seats))
    else:
        pass
    return reseats