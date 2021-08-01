import pytest
from src.regex import regex as regex


def test_rm1():
    assert regex.rm_trailing_numbers("a1234@gmail.com", 1) == "a@gmail.com"


# Or test multiple emails


def test_rm2():
    assert regex.rm_trailing_numbers("a1234@gmail.com", 5,) == "a1234@gmail.com"
    assert regex.rm_trailing_numbers("a1234@gmail.com", 1, 3) == "a1@gmail.com"


def test_extract():
    assert regex.extract_username("a@gmail.com") == "a"


# ==========Introduction to parametrize ==========


@pytest.mark.parametrize(
    "input_email,lb,ub,output_email",
    [
        ("a1234@gmail.com", 1, None, "a@gmail.com"),
        ("a1234@gmail.com", 5, None, "a1234@gmail.com"),
        ("a1234@gmail.com", 1, 3, "a1@gmail.com"),
    ],
)
def test_rm_trailing_numbers(input_email, lb, ub, output_email):
    assert (
        regex.rm_trailing_numbers(input_email, lb, ub) == output_email
    ), "something went wrong"
