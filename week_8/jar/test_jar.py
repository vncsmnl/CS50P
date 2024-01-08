from jar import Jar
import pytest

@pytest.fixture
def empty_jar():
    return Jar()

@pytest.fixture
def jar_with_capacity_10():
    return Jar(10)

def test_init():
    with pytest.raises(ValueError):
        Jar(-1)
    jar = Jar(0)
    assert jar.capacity == 0
    assert jar.size == 0
    jar = Jar(12)
    assert jar.capacity == 12
    assert jar.size == 0

def test_str(empty_jar):
    assert str(empty_jar) == ""
    empty_jar.deposit(1)
    assert str(empty_jar) == "🍪"
    empty_jar.deposit(11)
    assert str(empty_jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit(jar_with_capacity_10):
    with pytest.raises(ValueError):
        jar_with_capacity_10.deposit(-1)
    with pytest.raises(ValueError):
        jar_with_capacity_10.deposit(11)
    jar_with_capacity_10.deposit(3)
    assert jar_with_capacity_10.size == 3
    jar_with_capacity_10.deposit(7)
    assert jar_with_capacity_10.size == 10

def test_withdraw(jar_with_capacity_10):
    with pytest.raises(ValueError):
        jar_with_capacity_10.withdraw(-1)
    with pytest.raises(ValueError):
        jar_with_capacity_10.withdraw(1)
    jar_with_capacity_10.deposit(5)
    jar_with_capacity_10.withdraw(2)
    assert jar_with_capacity_10.size == 3
    with pytest.raises(ValueError):
        jar_with_capacity_10.withdraw(4)
    jar_with_capacity_10.withdraw(3)
    assert jar_with_capacity_10.size == 0
