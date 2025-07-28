from plates import is_valid
import pytest

@pytest.mark.parametrize("plate_input", [
    "CS50",
    "HELLO",
    "AAA222",
    "AB12",
    "AB",
    "AAAAAA",
    "HACS",
    "GOOFY",
])
def test_valid_plates(plate_input):
    assert is_valid(plate_input) == True

@pytest.mark.parametrize("plate_input", [
    "A",
    "ABCDEFG",
    "",
    "12",
    "A1",
    " 1",
    ".A",
    "CS.50",
    "CS 50",
    "HELLO!",
    "AB C",
    "AAA22A",
    "AB1A",
    "AAB2C",
    "NUMB3R",
    "CS05",
    "AA0",
    "00CS",
    "0A",
])
def test_invalid_plates(plate_input):
    assert is_valid(plate_input) == False
