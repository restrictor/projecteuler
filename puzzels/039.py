""" Integer right triangles

    Problem 39
    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
    there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?
"""

from time import perf_counter
start = perf_counter()

# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
from math import isqrt, gcd


def pythagorean_triples(perimeter: int) -> list:
    triples = []
    for m in range(isqrt(perimeter - 1) + 1):
        for n in range(1 + m % 2, min(m, isqrt(perimeter - m * m) + 1), 2):
            if not gcd(m, n) > 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                for k in range(1, perimeter // c + 1):
                    triples += [(k * a, k * b, k * c)]
    return triples


def integer_right_triangles_solutions(perimeter: int) -> None:
    solution_frequency = {}
    for pythagorean_triple in [triple for triple in pythagorean_triples(perimeter) if sum(list(triple)) < perimeter]:
        if sum(list(pythagorean_triple)) in solution_frequency:
            solution_frequency[sum(list(pythagorean_triple))] += 1
        else:
            solution_frequency[sum(list(pythagorean_triple))] = 1
    print(max(solution_frequency, key=solution_frequency.get))


integer_right_triangles_solutions(1000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 840
# Runtime of the program is 0.0008247000
