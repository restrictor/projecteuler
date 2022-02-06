""" Double-base palindromes

Problem 36
    The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from time import perf_counter
start = perf_counter()


def is_palindrome(number: str) -> bool:
    return number[::-1] == number


def sum_double_base_palindromes(n_bound: int) -> int:
    return sum([x for x in range(1, n_bound) if (is_palindrome(str(x)) and is_palindrome(bin(x)[2:]))])


print(sum_double_base_palindromes(1000000))

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 872187
# Runtime of the program is 0.2907981000

# this could be further improved by checking only the limited options for binary representation
# first digit starts with 1 and use combinations which results in very few options to check

