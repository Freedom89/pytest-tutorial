def factorial(x: int) -> int:
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

