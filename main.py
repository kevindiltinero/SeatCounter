from src import create
from src import count
from src import thefile
from src import execute



# This is creating the 2d array to represent the seating arrangement
# The count function is used directly after to test to see if all elements are there
seats = create.new_2d(1000, 1000)
counted_create = count.count_array(0, 1000, 0, 1000, seats)
print(counted_create)

# Trying out the exeution
commands = thefile.get_cmmds('inputfile.txt')
#seats = execute.execute_cmmds(seats, commands[7])
#print(seats)
#counted_after = count.count_array(0, 1000, 0, 1000, seats)
#print(counted_after)

for line in commands:
    seats = execute.execute_cmmds(seats, line)
counted_after = count.count_array(0, 1000, 0, 1000, seats)
print(counted_after)


#counted_after = count.count_array(0, 1000, 0, 1000, seats)
#print(counted_after)

#print(seats)
#counted_after = count.count_array(0, 1000, 0, 1000, seats)
#print(counted_after)


