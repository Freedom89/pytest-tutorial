import pytest
import src.demo_mock
from src.demo_mock import add_minus_10, get_constant

# Constants


def test_replace_constant(mocker):
    mocker.patch.object(src.demo_mock, "CONSTANT", 123)
    expected = 246
    actual = get_constant()  # you would expect 200
    assert actual == expected, "something went wrong"


def test_replace_function(mocker):
    mocker.patch("src.demo_mock.add", return_value=200)
    actual = add_minus_10(10, 20)  # you would expect 20
    expected = 190
    assert actual == expected, "something went wrong"
