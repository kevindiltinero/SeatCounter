from tests import tests

def test_sizeafteroccupy():
    count = tests.counted_occupy
    assert count == 5

