from src import create
from src import count
from src import thefile
from src import execute



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
    counter_occupied = 1000000 - counted_after
    return counter_occupied

results = main(1000, 1000, 'inputfile.txt')