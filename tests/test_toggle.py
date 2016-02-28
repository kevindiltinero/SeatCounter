import main

def test_toggle():
    temporary = main.final_seats
    assert temporary == [[1, 1, 1], [1, 0, 0], [1, 0, 0]]