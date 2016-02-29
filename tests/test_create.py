from tests import tests

def test_count_after_create():
    count = tests.counted_create
    next_count = tests.counted_create_again
    assert count == 9
    assert next_count == 25

