from src import create
from src import occupy
from src import count

seats = create.new_2d(5, 5)
print(seats)

occupy_seats = occupy.occupy_seats(2, 3, 2, 3, seats)
print(occupy_seats)

counted_seats = count.count_array(0, 5, 0, 5, occupy_seats)
print(counted_seats)