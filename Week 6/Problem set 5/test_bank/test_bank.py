from bank import value
import pytest

@pytest.mark.parametrize("greeting_input, expected_output",
    [("hi", 20),
    ("Hi", 20),
    ("how are you?", 20),
    ("Howdy", 20),
    ("hey", 20),
    (" h", 20)])
def test_value_others(greeting_input, expected_output):
    assert value(greeting_input) == expected_output

@pytest.mark.parametrize("greeting_input, expected_output",
    [("whats up", 100),
     ("Greetings", 100),
     ("123", 100),
     ("", 100),
     ( "good morning", 100)])
def test_hello(greeting_input, expected_output):
    assert value(greeting_input) == expected_output
