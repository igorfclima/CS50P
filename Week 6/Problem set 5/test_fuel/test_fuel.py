import pytest
from fuel import convert, gauge
@pytest.mark.parametrize("fraction_str, expected_float", [
    ("1/4", 0.25),
    ("3/4", 0.75),
    ("1/2", 0.5),
    ("0/100", 0.0),
    ("100/100", 1.0),
    ("1/3", 1/3),
    ("2/3", 2/3),
    ("50/100", 0.5),
    ("1/1", 1.0)
])
def test_convert_valid_fractions(fraction_str, expected_float):
    assert convert(fraction_str) == expected_float

@pytest.mark.parametrize("invalid_fraction_str", [
    "cat/dog",
    "3/dog",
    "cat/4",
    "1/2/3",
    "1",
    "10/2",
    "100/1",
    "2/1"
])
def test_convert_value_error(invalid_fraction_str):
    with pytest.raises(ValueError):
        convert(invalid_fraction_str)

@pytest.mark.parametrize("zero_denominator_fraction_str", [
    "1/0",
    "0/0",
    "50/0"
])
def test_convert_zero_division_error(zero_denominator_fraction_str):
    with pytest.raises(ZeroDivisionError):
        convert(zero_denominator_fraction_str)

@pytest.mark.parametrize("float_percentage, expected_output", [
    (0.0, "E"),
    (0.01, "E"),
    (0.001, "E"),
    (0.000, "E")
])
def test_gauge_e(float_percentage, expected_output):
    assert gauge(float_percentage) == expected_output

@pytest.mark.parametrize("float_percentage, expected_output", [
    (1.0, "F"),
    (0.99, "F"),
    (0.995, "F"),
    (0.985, "F")
])
def test_gauge_f(float_percentage, expected_output):
    assert gauge(float_percentage) == expected_output

@pytest.mark.parametrize("float_percentage, expected_output", [
    (0.25, "25%"),
    (0.5, "50%"),
    (0.75, "75%"),
    (0.33, "33%"),
    (0.333333333, "33%"),
    (0.666666666, "67%")
])
def test_gauge_percentage(float_percentage, expected_output):
    assert gauge(float_percentage) == expected_output
