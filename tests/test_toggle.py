import main

def test_toggle():
    temporary = main.toggled_seats

    count = main.counted_toggle

    assert temporary == [[0, 0, 1], [0, 0, 1], [1, 1, 1]]
    assert count == 4