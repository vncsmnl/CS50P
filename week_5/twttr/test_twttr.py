from twttr import shorten

def test_shorten():y

    # Test cases for the shorten function

    # Test case 1: Empty string should return an empty string
    assert shorten("") == ""

    # Test case 2: String with only vowels should return an empty string
    assert shorten("aeiou") == ""

    # Test case 3: String with only capital vowels should return an empty string
    assert shorten("AEIOU") == ""

    # Test case 4: Test with a regular string
    assert shorten("twitter") == "twttr"

    # Test case 5: Test with a mixed case string
    assert shorten("tWitTer") == "tWtTr"

    # Test case 6: Test with a string containing special characters
    assert shorten("What's your name?") == "Wht's yr nm?"

    # Test case 7: Test with alphanumeric characters
    assert shorten("1a2be") == "12b"

if __name__ == "__main__":
    test_shorten()
