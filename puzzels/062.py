""" Cubic permutations

    Problem 62
    The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
    In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

    Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from time import perf_counter
start = perf_counter()

from math import ceil


def is_perfect_cube(n: int) -> bool:
    return int(round(abs(n) ** (1. / 3))) ** 3 == abs(n)


def smallest_permutations_cube() -> None:
    bound, smallest_candidate, found, cubes = 9999999999999999, 2, False, {}
    while smallest_candidate < bound:
        sorted_digits = ''.join(sorted(list(str(smallest_candidate ** 3))))
        if sorted_digits in cubes.keys():
            cubes[sorted_digits][0] += 1
        else:
            cubes[sorted_digits] = [1, smallest_candidate]
        if cubes[sorted_digits][0] == 5 and not found:
            bound, found = 10 ** (ceil(len(str(smallest_candidate ** 3)) / 3) + 1), True
        smallest_candidate += 1
    print([candidate for candidate in cubes.values() if candidate[0] == 5][0])


smallest_permutations_cube()

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# [5, 5027]
# Runtime of the program is 0.2186777000


