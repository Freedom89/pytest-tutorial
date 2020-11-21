import time as time

# define a constant
CONSTANT = 100
# define a function
def get_constant():
    return CONSTANT * 2


def get_time_now() -> int:
    return int(time.time())


def add(x: int, y: int) -> int:
    return x + y


def add_minus_10(x: int, y: int) -> int:
    value = add(x, y)
    return value - 10

