import pytest


@pytest.fixture
def put_whatever_name_you_wish():
    return "anyvalue"


def test_value(put_whatever_name_you_wish):
    assert put_whatever_name_you_wish == "anyvalue", "something went wrong"
