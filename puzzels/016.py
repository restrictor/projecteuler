""" Power digit sum

    Problem 16
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
"""

from time import perf_counter
start = perf_counter()


def power_digit_sum(number: int) -> int:
    return sum(int(digit) for digit in str(2**number))


print(power_digit_sum(1000))

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 1366
# Runtime of the program is 0.0000906000
