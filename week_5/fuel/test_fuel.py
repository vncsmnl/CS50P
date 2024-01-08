import pytest
from fuel import convert, gauge

class TestFuelFunctions:
    @pytest.mark.parametrize("input_str, expected_output", [("3/4", 75), ("1/3", 33), ("2/3", 67),
                                                            ("0/100", 0), ("100/100", 100), ("99/100", 99)])
    def test_convert_valid_cases(self, input_str, expected_output):
        assert convert(input_str) == expected_output

    @pytest.mark.parametrize("invalid_input", ["x/y", "three/four", "10/3", "1.5/4", "5-4"])
    def test_convert_invalid_cases(self, invalid_input):
        with pytest.raises(ValueError):
            convert(invalid_input)

    def test_convert_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            convert("1/0")

    @pytest.mark.parametrize("value, expected_output", [(0, "E"), (1, "E"), (100, "F"), (99, "F"),
                                                        (2, "2%"), (40, "40%"), (98, "98%")])
    def test_gauge(self, value, expected_output):
        assert gauge(value) == expected_output
