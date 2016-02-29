from tests import tests


def test_decode_file():
    temporary = tests.check_commands
    assert temporary[5] == ['occupy', '226', '196', 'through', '599', '390']

