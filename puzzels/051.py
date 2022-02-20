""" Prime digit replacements

    Problem 51
    By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible
    values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the
    first example having seven primes among the ten generated numbers, yielding the
    family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently, 56003, being the
    first member of this family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with
    the same digit, is part of an eight prime value family.
"""

from time import perf_counter
start = perf_counter()

# Replacing n digits (with/to similar value) in a m digit number will result in a change in digit sum.
# The digitsum must not be divisible by 3 and to do so to just replace one digit will not work.
# The last value of a prime cannot be replaced by 8 different numbers, so it cannot be replaced.
# if the digitsum is changed by replacing 3 digits the digit sum will not be divisible by three.

# n ≡ x (mod 3) -> m ≡ x + n_digits * ( i ) (mod 3) for i in (0,1,2,3,4,5,6,7,8,9)
# It is clear that only setting i to 3 will hold similar modulo outcome which will not be divisible by 3.

import itertools
from lib.library import get_list_of_primes
import collections


def replace_digits(string: str, mask: list, value: str) -> str:
    return "".join([string[i] if mask[i] != 1 else value for i in range(len(string))])


def similar(string: str, mask: list) -> int:
    return len(set([string[i] for i in range(len(string)) if mask[i] == 1]))


def get_unique_key_from_value(d: dict, val: int) -> str | None:
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]


def digit_length_prime_digit_replacements(n_digits: int, pr: list) -> tuple[str | None, list, list[str]] | None:
    masks = list(itertools.product([0, 1], repeat=n_digits - 1))

    # remove 2, 4 repeated digits (will be divisible by 3)
    if n_digits == 6:
        masks = [x for x in masks if sum(x) == 3]

    for mask in masks:
        digit_length_selection = [p for p in pr if 10 ** (n_digits - 1) - 1 < p < 10 ** n_digits]
        similar_digits = [p for p in digit_length_selection if similar(str(p), list(mask) + [0]) == 1]
        mask_with_x = [replace_digits(str(y), list(mask) + [0], "X") for y in similar_digits]
        if 8 in collections.Counter(mask_with_x).values():
            return get_unique_key_from_value(collections.Counter(mask_with_x), 8), similar_digits, mask_with_x


def smallest_prime_digit_replacements(n: int, lower: int, upper: int) -> None:

    # only take numbers with more than 2 repeating digits (see explanation above)
    primes = [p for p in get_list_of_primes(n) if len(str(p)) - len(set(list(str(p)))) > 2]

    # 3 and 4 digits not possible because number will always be divisible by 3 -> lower set to at least 5
    for digit_length in range(lower, upper):
        candidates = digit_length_prime_digit_replacements(digit_length, primes)
        if candidates:
            for masked_numbers, numbers in zip(candidates[2], candidates[1]):
                if all(str(masked_numbers)[i] == candidates[0][i] for i in range(len(candidates[0]))):
                    print(masked_numbers, numbers)
            break


smallest_prime_digit_replacements(1000000, 5, 10)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# X2X3X3 121313
# X2X3X3 222323
# X2X3X3 323333
# X2X3X3 424343
# X2X3X3 525353
# X2X3X3 626363
# X2X3X3 828383
# X2X3X3 929393
# Runtime of the program is 0.2574683000
