from tests import tests

def test_toggle():
    temporary = tests.toggled_seats
    assert temporary == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]