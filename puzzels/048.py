""" Self powers

    Problem 48
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

from time import perf_counter
start = perf_counter()


def self_power(n: int) -> None:
    total = 0
    for index in range(1, n + 1):
        total += index ** index
    print(str(total)[-10:])


self_power(1000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 9110846700
# Runtime of the program is 0.0091422000
