import pytest


@pytest.mark.function
def test_one(function_fixture):
    assert function_fixture


@pytest.mark.function
def test_two(function_fixture):
    assert function_fixture
