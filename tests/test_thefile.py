import main

def test_decode_file():
    temporary = main.check_commands
    assert len(temporary) == 300
    assert temporary[5] == ['occupy', '226', '196', 'through', '599', '390']

