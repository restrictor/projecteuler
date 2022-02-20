""" Combinatoric selections

    Problem 53
    There are exactly ten ways of selecting three from five, 12345:

        123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    In combinatorics, we use the notation, (5  3)=10.
    In general, (n r)=n!/(r!(n−r)!), where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1
    It is not until n=23, that a value exceeds one-million: (23  10)=1144066.
    How many, not necessarily distinct, values of (n  r) for 1≤n≤100, are greater than one-million?
 """

from time import perf_counter
start = perf_counter()

# from solution of problem 034
from lib.library import factorial


def count_greater_than_one_millon(n_r_bound: int, greater_than: int) -> None:
    count, factorials = 0, {}
    factorials = {}
    for n_r in range(0, n_r_bound + 1):
        factorials[n_r] = factorial(n_r)
    for n in range(22, n_r_bound + 1):
        for r in range(1, n + 1):
            if factorials[n] / ((factorials[n - r]) * (factorials[r])) > greater_than:
                count += 1
    print(count)


count_greater_than_one_millon(100, 1000000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 4075
# Runtime of the program is 0.0046759000
