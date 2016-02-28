from src import create
from src import count
from src import thefile
from src import execute
from src import occupy
from src import toggle


def main(x, y, file):
    #Create it
    seats = create.new_2d(x, y)

    #Count it
    counted_start = count.count_array(x, y, seats)
    print(counted_start)

    #Get the commands
    commands = thefile.get_cmmds(file)

    #The execution
    for line in commands:
        seats = execute.execute_cmmds(seats, line)
    counted_after = count.count_array(x, y, seats)
    print(counted_after)

#main(1000, 1000, 'inputfile.txt')

check_commands = thefile.get_cmmds('inputfile.txt')
print(check_commands[5])

seats = create.new_2d(3, 3)
newseats = occupy.occupy_seats(1, 1, 2, 2, seats)
print(newseats)
final_seats = toggle.toggle_it(0, 0, 2, 2, newseats)
print(final_seats)
