import main

def test_count_after_create():
    count = main.counted_create
    next_count = main.counted_create_again
    assert count == 9
    assert next_count == 25

