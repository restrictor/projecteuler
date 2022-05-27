""" Counting rectangles

    Problem 85
    By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

        x 0 0       x x 0       x x x
        0 0 0       0 0 0       0 0 0
          6           4           2

        x 0 0       x x 0       x x x
        x 0 0       x x 0       x x x
          3           2           1

    Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the
    grid with the nearest solution.
"""

from time import perf_counter
start = perf_counter()

# we can make n*(n+1)/2 rectangles in one dimension -> n*(n+1)/2 * m*(m+1)/2 in two dimensions
# for a 2000x1 grid we have: 2000*2001/2 * 1*(1+1)/2 = 2001000 -> n=1, m=2000 -> n_grid = 2000
# we can solve for m in n*(n+1)/2 * m*(m+1)/2 = x -> n^2 + n = 4x/(m^2 + m) and n > 0 assuming
# then for values of n we are looking for values m < sqrt(4x/(n^2 + n)) so we can brute force.

from math import ceil


def get_closest_grid(aim: int) -> None:
    min_diff = aim
    bound = ceil((aim * 2) ** 0.5)
    solution = []
    for n in range(1, bound):
        for m in range(1, ceil(((4 * aim) / (n ** 2 + n)) ** 0.5)):
            n_rectangles = n*(n+1)/2 * m*(m+1)/2
            if abs(aim - n_rectangles) < min_diff:
                min_diff = abs(aim - n_rectangles)
                solution = [n_rectangles, min_diff, n, m, n * m]
            else:
                pass
    print(solution)


get_closest_grid(2000000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# [1999998.0, 2.0, 36, 77, 2772]
# Runtime of the program is 0.0082970000
