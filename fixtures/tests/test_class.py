import pytest


@pytest.mark.class_
@pytest.mark.usefixtures("class_fixture")
class TestMyFixtures:
    def test_one(self):
        assert self

    def test_two(self):
        assert self


@pytest.mark.class_
@pytest.mark.usefixtures("class_fixture")
class TestMyFixturesAgain:
    def test_three(self):
        assert self

    def test_four(self):
        assert self
