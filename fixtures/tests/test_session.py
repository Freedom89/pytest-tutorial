import pytest


@pytest.mark.session
def test_one(session_fixture):
    assert session_fixture


@pytest.mark.session
def test_two(session_fixture):
    assert session_fixture
