import pytest


@pytest.mark.parametrize(
    "input,another_input,output",
    [((1, 1), 2, 4), ((2, 4), 4, 10), ((4, 10), 100, 114)],
)
def test_addition(input, another_input, output):
    assert sum(input) + another_input == output, "something went wrong"
