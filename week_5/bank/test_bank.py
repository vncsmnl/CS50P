from bank import value

def test_value():
    # Test cases for greetings with no positive value
    assert value("Hello") == 0
    assert value(" Hello ") == 0
    assert value("Hello, Newman") == 0
    # Test cases for positive statements
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100
    assert value("What's up?") == 100
