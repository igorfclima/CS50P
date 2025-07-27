from bank import value

def test_hundreds():
    assert value("What's happening?") == "$100"
def test_hello():
    assert value("Hello ") == "$0"
