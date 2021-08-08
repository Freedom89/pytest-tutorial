import pytest


@pytest.mark.session
def test_three(session_fixture):
    assert session_fixture


@pytest.mark.session
def test_four(session_fixture):
    assert session_fixture
