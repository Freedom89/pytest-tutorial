import pytest
import src.mock
from src.mock import add_minus_10, get_constant

# Constants


def test_replace_constant(mocker):
    mocker.patch.object(src.mock, "CONSTANT", 123)
    expected = 246
    actual = get_constant()  # you would expect 200
    assert actual == expected, "something went wrong"


def test_replace_function(mocker):
    mocker.patch("src.mock.add", return_value=200)
    actual = add_minus_10(10, 20)  # you would expect 20
    expected = 190
    assert actual == expected, "something went wrong"
