from classiq import *


@qfunc
def main(x: Output[QNum], y: Output[QNum]):

    allocate(4, x)
    hadamard_transform(x)  # creates a uniform superposition
    y |= x**2 + 1