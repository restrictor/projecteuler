""" Prime permutations

    Problem 49
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
    is unusual in two ways: (i) each of the three terms are prime, and,
                            (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting
    this property, but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from time import perf_counter
start = perf_counter()


# solution for problem 007
from lib.library import get_list_of_primes


def get_candidates_arithmetic_prime_permutations(lower_bound: int, upper_bound: int) -> dict:
    primes = set([x for x in get_list_of_primes(upper_bound) if x > lower_bound])
    candidates = {}
    for prime in primes:
        key = "".join(sorted(list(str(prime))))
        if key in candidates.keys():
            candidates[key] += [prime]
        else:
            candidates[key] = [prime]

    # remove the candidates permutations with 2 or 1 members
    for key, value in list(candidates.items()):
        if len(value) < 3:
            del candidates[key]
    return candidates


def is_arithmetic_prime_permutations(prime_permutations: dict) -> (bool, list):
    for x1 in prime_permutations:
        for x2 in [z for z in prime_permutations if z > x1]:
            for x3 in [zz for zz in prime_permutations if zz > x2]:
                if x2 - x1 == x3 - x2:
                    return x2 - x1 == x3 - x2, [x1, x2, x3]
    return False


def get_arithmetic_prime_permutations(lower_bound: int, upper_bound: int) -> None:
    candidates = get_candidates_arithmetic_prime_permutations(lower_bound, upper_bound)
    distances = {}
    for k, v in list(candidates.items()):
        x = sorted(v)
        distances[k] = []
        if is_arithmetic_prime_permutations(x):
            print("".join([str(x) for x in is_arithmetic_prime_permutations(x)[1]]))


get_arithmetic_prime_permutations(1487, 10000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 296962999629
# Runtime of the program is 0.0060925000


