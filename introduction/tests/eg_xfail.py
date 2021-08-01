import pytest


@pytest.mark.xfail(strict=True)
def test_function():
    assert 1 == 2, "something went wrong"

