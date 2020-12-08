from src import simple_math


def test_factorial():
    assert simple_math.factorial(3) == 6, "response is incorrect"


def tet_factorial():
    # this will not get test
    assert simple_math.factorial(10) == 6, "response is incorrect"
