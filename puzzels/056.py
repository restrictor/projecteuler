""" Powerful digit sum

    Problem 56
    A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably
    large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

    Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

from time import perf_counter
start = perf_counter()


def max_digital_sum(n_bound: int) -> None:
    max_sum = 0
    for a in range(10, n_bound):
        for b in range(10, n_bound):
            candidate = sum([int(x) for x in str(a ** b)])
            if candidate > max_sum:
                max_sum = candidate
    print(max_sum)


max_digital_sum(100)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 972
# Runtime of the program is 0.1013995000
