# This is creating the 2d array to represent the seating arrangement
# The count function is used directly after to test to see if all elements are there
seats = create.new_2d(1000, 1000)
counted_create = count.count_array(0, 1000, 0, 1000, seats)
print(counted_create)

# Trying out the exeution
commands = thefile.get_cmmds('inputfile.txt')
seats = execute_cmmds(seats, commands[6])
#print(seats)
counted_after = count.count_array(0, 1000, 0, 1000, seats)

counted_after = count.count_array(0, 1000, 0, 1000, seats)
#print(counted_after)

#print(seats)
counted_after = count.count_array(0, 1000, 0, 1000, seats)
#print(counted_after)


