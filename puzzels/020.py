""" Factorial digit sum

    Problem 20
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
"""

from time import perf_counter
start = perf_counter()


def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n-1)


def factorial_digit_sum(number: int) -> int:
    return sum(int(digit) for digit in str(factorial(number)))


print(factorial_digit_sum(100))

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 648
# Runtime of the program is 0.0001062000
