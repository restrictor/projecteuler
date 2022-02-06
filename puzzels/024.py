""" Lexicographic permutations

    Problem 24
    A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of
    the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call
     it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from time import perf_counter
start = perf_counter()

import itertools


def lexicographic_permutations(digits: list, n: int) -> None:
    permutations = list(itertools.permutations(digits, len(digits)))[n - 1]
    print(''.join([str(x) for x in list(permutations)]))


lexicographic_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 2783915460
# Runtime of the program is 0.5885376000
