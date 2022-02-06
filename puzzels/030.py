""" Digit fifth powers

    Problem 30
    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

        1634 = 1^4 + 6^4 + 3^4 + 4^4
        8208 = 8^4 + 2^4 + 0^4 + 8^4
        9474 = 9^4 + 4^4 + 7^4 + 4^4

    As 1 = 1^4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

from time import perf_counter
start = perf_counter()


def upper_bound_digits(power: int) -> int:
    n_digits = 1

    # n*9^5 (fifth power digit sum) doesn't grow so fast as number with n digits
    while n_digits <= len(str(sum([int(i) ** power for i in [9] * n_digits]))):
        n_digits += 1
    return sum([int(i) ** power for i in [9] * (n_digits - 1)])


def digit_fifth_powers_sum_is_number(n: int, power: int) -> bool:
    digit_fifth_powers_sum = 0
    for i in str(n):
        digit_fifth_powers_sum += int(i) ** power
    return digit_fifth_powers_sum == n


def sum_of_digit_fifth_powers_sum_is_number(power: int) -> None:
    digit_fifth_powers_sum_is_number_sum = 0
    for candidate in range(2, upper_bound_digits(power)):
        if digit_fifth_powers_sum_is_number(candidate, power):
            digit_fifth_powers_sum_is_number_sum += candidate
    print(digit_fifth_powers_sum_is_number_sum)


sum_of_digit_fifth_powers_sum_is_number(5)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 443839
# Runtime of the program is 0.7203072000

