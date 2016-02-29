import tests


def test_count_after_create():
    count = tests.counted_create
    next_count = tests.counted_create_again
    assert count == 9
    assert next_count == 25


def test_count():
    count = tests.counted_create
    next_count = tests.counted_create_again
    assert count == 9


def test_sizeafteroccupy():
    count = tests.counted_occupy
    assert count == 5


def test_toggle():
    temporary = tests.toggled_seats
    assert temporary == [[0, 0, 1], [0, 0, 1], [1, 1, 1]]


def test_sizeafterempty():
    count = tests.counted_emptied
    assert count == 9


def test_decode_file():
    temporary = tests.check_commands
    assert temporary[5] == ['occupy', '226', '196', 'through', '599', '390']

def test_execute():
    count = main.results
    assert count == 400410

