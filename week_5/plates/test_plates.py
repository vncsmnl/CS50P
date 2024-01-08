from plates import is_valid

def test_is_valid():
    # Valid plates
    assert is_valid("CS50"), "Test case 1 failed"
    assert is_valid("ECTO88"), "Test case 2 failed"
    assert is_valid("NRVOUS"), "Test case 3 failed"

    # Invalid plates
    assert not is_valid("CS05"), "Test case 4 failed"
    assert not is_valid("CS50P2"), "Test case 5 failed"
    assert not is_valid("123456"), "Test case 6 failed"
    assert not is_valid("PI3.14"), "Test case 7 failed"
    assert not is_valid("H"), "Test case 8 failed"
    assert not is_valid("OUTATIME"), "Test case 9 failed"
    assert not is_valid("ABC?!-"), "Test case 10 failed"
