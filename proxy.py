


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