from tests import tests

def test_sizeafterempty():
    count = tests.counted_emptied
    assert count == 9

