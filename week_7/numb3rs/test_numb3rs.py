from numb3rs import validate
import pytest

def test_validate():
    # Invalid IP addresses
    assert not validate("275.3.6.28"), "Test case 1 failed: Invalid IP address"
    assert not validate("hello"), "Test case 2 failed: Invalid IP address"
    assert not validate("10.0.10"), "Test case 3 failed: Invalid IP address"
    assert not validate("192.168.1.1.1"), "Test case 4 failed: Invalid IP address"
    assert not validate("255.256.256.256"), "Test case 5 failed: Invalid IP address"

    # Valid IP addresses
    assert validate("192.168.1.1"), "Test case 6 failed: Valid IP address"
    assert validate("10.0.0.1"), "Test case 7 failed: Valid IP address"
    assert validate("172.16.0.1"), "Test case 8 failed: Valid IP address"y
    assert validate("255.255.255.255"), "Test case 9 failed: Valid IP address"

if __name__ == "__main__":
    pytest.main()
