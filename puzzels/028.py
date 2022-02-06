""" Number spiral diagonals

    Problem 28
    Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from time import perf_counter
start = perf_counter()


def sum_number_spiral_diagonals(n: int) -> None:
    sum_n = 1
    for i in range(3, n + 1, 2):

        # for a (sub) square: right_top + left_top + left_down + right_down
        # = i ** 2 + i ** 2 - (i - 1) + i ** 2 - 2 * (i - 1) + i ** 2 - 3 * (i - 1)
        # = 4 * (i ** 2) - 6 * (i - 1)
        # = 4x^2 - 6(x-1)
        sum_n += 4 * (i ** 2) - 6 * (i - 1)
    print(sum_n)


sum_number_spiral_diagonals(1001)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 669171001
# Runtime of the program is 0.0002334000
