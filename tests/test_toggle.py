from tests import tests

def test_toggle():
    temporary = tests.toggled_seats
    assert temporary == [[0, 0, 1], [0, 0, 1], [1, 1, 1]]