from um import count

def test_count():
    assert count("hello world") == 0, "Test case 1 failed"
    assert count("yummy") == 0, "Test case 2 failed"
    assert count("umum") == 0, "Test case 3 failed"

    assert count("hello, um, world") == 1, "Test case 4 failed"
    assert count("um um um") == 3, "Test case 5 failed"
    assert count("um?") == 1, "Test case 6 failed"
    assert count("Um, thanks for the album.") == 1, "Test case 7 failed"
    assert count("Um, thanks, um...") == 2, "Test case 8 failed"

if __name__ == "__main__":
    test_count()
