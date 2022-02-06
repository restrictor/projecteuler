""" Lattice paths

    Problem 15
    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there
     are exactly 6 routes to the bottom right corner.

    (see https://projecteuler.net/problem=15)

    How many such routes are there through a 20×20 grid?
"""

from time import perf_counter
start = perf_counter()


# walk to the grid and add the possible traveled paths (left and up)
def lattice_paths(n: int = 20) -> None:
    row = [1] * (n + 1)
    sol = row
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sol[j] = sol[j - 1] + row[j]
        row = sol
    print(sol[-1])


lattice_paths(20)
end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 137846528820
# Runtime of the program is 0.0000884000

start = perf_counter()

# a more direct approach (which is fast but deals with very large numbers for large n)
import math

n_grid = 20
print(math.factorial(2 * n_grid) / (math.factorial(n_grid)) ** 2)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")
# 137846528820.0
# Runtime of the program is 0.0000200000
