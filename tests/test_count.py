from tests import tests

def test_count():
    count = tests.counted_create
    next_count = tests.counted_create_again
    assert count == 9