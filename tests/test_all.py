from src import create
from src import count
from src import thefile
from src import occupy
from src import toggle
from src import empty

def test_count_after_create():
    count = main.counted_create
    next_count = main.counted_create_again
    assert count == 9
    assert next_count == 25

def test_count():
    count = tests.counted_create
    next_count = tests.counted_create_again
    assert count == 9
    assert next_count == 25

def test_sizeafteroccupy():
    count = main.counted_occupy
    assert count == 5

def test_sizeafterempty():
    count = main.counted_emptied
    assert count == 9

def test_toggle():
    temporary = main.toggled_seats

    count = main.counted_toggle

    assert temporary == [[0, 0, 1], [0, 0, 1], [1, 1, 1]]
    assert count == 4

def test_decode_file():
    temporary = main.check_commands
    assert len(temporary) == 300
    assert temporary[5] == ['occupy', '226', '196', 'through', '599', '390']

def test_execute():
    count = main.results
    assert count == 400410

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
