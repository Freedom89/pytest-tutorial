import pytest


@pytest.mark.module
def test_three(module_fixture):
    assert module_fixture


@pytest.mark.module
def test_four(module_fixture):
    assert module_fixture
