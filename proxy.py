# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
#occupied_seats = occupy.occupy_seats(0, 3, 0, 3, seats)
#counted_occupy = count.count_array(0, 5, 0, 5, seats)
#print(occupied_seats)

# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
#toggled_seats = toggle.toggle_it(0, 5, 0, 5, seats)
#counted_toggle = count.count_array(0, 5, 0, 5, seats)
#print(toggled_seats)

# This is alternating the array to add the seats that become occupied
# The count function is used directly after to test that the change occured
#emptied_seats = empty.empty_it(0, 5, 0, 5, occupied_seats)
#counted_emptied = count.count_array(0, 5, 0, 5, emptied_seats)
#print(emptied_seats)


listed = [[0 for x in range(3)] for x in range(3)]

print(listed)

#1,1   through 22

for i in range(1, 3):
     for j in range(1, 3):
         listed[i][j] = 1
print(listed)

count = 0
for i in range(0, 3):
    for j in range(0, 3):
        if listed[i][j] == 1:
            count += 1
print(count)

for i in range(0, 3):
    for j in range(0, 3):
        if listed[i][j] == 1:
            listed[i][j] = 0
        elif listed[i][j] == 0:
            listed[i][j] = 1
        else:
            pass

print(listed)

count = 0
for i in range(0, 3):
    for j in range(0, 3):
        if listed[i][j] == 1:
            count += 1
print(count)


for i in range(0, 3):
     for j in range(0, 3):
         listed[i][j] = 0
print(listed)

count = 0
for i in range(0, 3):
    for j in range(0, 3):
        if listed[i][j] == 1:
            count += 1
print(count)