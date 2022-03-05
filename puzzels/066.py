""" Diophantine equation

Problem 66
Consider quadratic Diophantine equations of the form:

    x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

    3^2 – 2×2^2 = 1
    2^2 – 3×1^2 = 1
    9^2 – 5×4^2 = 1
    5^2 – 6×2^2 = 1
    8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""

from time import perf_counter
start = perf_counter()

# PELL’S EQUATION, II, KEITH CONRAD https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pelleqn2.pdf
# "For each positive solution to x^2 - dy^2 = +- 1, there is a convergent p/q to √d such that x = p and y = q."

# solution for problem 065
from lib.library import continued_fraction_n


def continued_fraction_terms(s: float) -> list:
    m0, d0, a0 = 0, 1, int(s ** 0.5)
    i, m, d, a, terms = 0, m0, d0, a0, [a0]
    while True:
        m = d * a - m
        d = (s - m ** 2) / d
        a = int((a0 + m) / d)
        terms.append(a)
        i += 1
        if a == 2 * a0:
            break
    return terms


def max_x_min_solution_diophantine_equation() -> None:
    max_x, D = 0, 0
    for i in range(2, 1001):
        if int(i**0.5) ** 2 != i:
            terms = continued_fraction_terms(i)
            x = int(continued_fraction_n(terms[:len(terms) - 1]).numerator)
            y = int(continued_fraction_n(terms[:len(terms) - 1]).denominator)

            # positive bell equation
            if len(terms) % 2:
                x, y = 2 * x ** 2 + 1, 2 * x * y

            # if solution
            if x ** 2 - i * y ** 2 == 1 or x ** 2 - i * y ** 2 == -1:
                min_x = x
                if min_x > max_x:
                    D, max_x = i, min_x

    print(max_x, D)


max_x_min_solution_diophantine_equation()

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 2865454435422583218 661
# Runtime of the program is 0.1509553000
