""" Powerful digit counts

    Problem 63
    The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is
    a ninth power.

    How many n-digit positive integers exist which are also an nth power?
"""

from time import perf_counter
start = perf_counter()

# digits(n) must be lower than 10 to hold n^p = p-digits and bound p we can calculate


def bound_power() -> int:
    max_allowed_digits = 1
    while len(str(9**max_allowed_digits)) >= max_allowed_digits:
        max_allowed_digits += 1
    return max_allowed_digits - 1


def is_perfect_n_cube(number: int, power: int) -> bool:
    return int(round(abs(number) ** (1. / power))) ** power == abs(number)


def count_powerful_digit() -> None:
    total, powerful_digits = 0, {}
    for power in range(1, bound_power() + 1):
        for num in range(1, 10):
            if is_perfect_n_cube(num ** power, len(str(num ** power))) and int(num ** power) not in powerful_digits:
                powerful_digits[int(num ** power)] = True
                total += 1
    print(total)


count_powerful_digit()

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 49
# Runtime of the program is 0.0004607000
