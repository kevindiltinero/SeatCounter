from src import create
from src import count
from src import thefile
from src import execute
from src import occupy
from src import toggle
from src import empty


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
print(results)

#THE TEST FOR THE CREATE FUNCTION
seats = create.new_2d(3, 3)
counted_create = count.count_array(3, 3, seats)
seats = create.new_2d(5, 5)
counted_create_again = count.count_array(5, 5, seats)

#TEST FOR OCCUPY
# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
seats = create.new_2d(3, 3)
occupied_seats = occupy.occupy_seats(0, 0, 1, 1, seats)
counted_occupy = count.count_array(3, 3, occupied_seats)

#TEST FOR TOGGLE
# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
toggled_seats = toggle.toggle_it(0, 0, 2, 2, occupied_seats)
counted_toggle = count.count_array(3, 3, toggled_seats)

#TEST FOR EMPTY
# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
emptied_seats = empty.empty_it(0, 0, 2, 2, toggled_seats)
counted_emptied = count.count_array(3, 3, emptied_seats)

#TEST THE FILE DECODE ()
check_commands = thefile.get_cmmds('inputfile.txt')
print(check_commands[5])

#TEST THE EXECUTING FUNCTION
