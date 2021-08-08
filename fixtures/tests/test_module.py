import pytest


@pytest.mark.module
def test_one(module_fixture):
    assert module_fixture


@pytest.mark.module
def test_two(module_fixture):
    assert module_fixture
