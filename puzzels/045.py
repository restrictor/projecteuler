""" Triangular, pentagonal, and hexagonal

    Problem 45
    Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

    Triangle	 	T_n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
    Pentagonal	 	P_n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
    Hexagonal	 	H_n=n(2n−1)	 	1, 6, 15, 28, 45, ...
    It can be verified that T_285 = P_165 = H_143 = 40755.

    Find the next triangle number that is also pentagonal and hexagonal.
"""

from time import perf_counter
start = perf_counter()

import math

# seems that tri in hex so only check for hex and then pen


def hexagonal(number: int) -> int:
    return number * (2 * number - 1)


def is_pentagonal(n: int) -> bool:
    candidate = 1 / 6 * (1 + math.sqrt(1 + 24 * n))
    return candidate == int(candidate)


def next_triangular_pentagonal_hexagonal(from_number: int) -> None:
    i = from_number
    while 1:
        if is_pentagonal(hexagonal(i)):
            print(hexagonal(i))
            return
        i += 1


next_triangular_pentagonal_hexagonal(145)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 1533776805
# Runtime of the program is 0.0232841000