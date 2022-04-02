""" Digit factorial chains

    Problem 74
    The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

        1! + 4! + 5! = 1 + 24 + 120 = 145

    Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns
    out that there are only three such loops that exist:

        169 → 363601 → 1454 → 169
        871 → 45361 → 871
        872 → 45362 → 872

    It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

        69 → 363600 → 1454 → 169 → 363601 (→ 1454)
        78 → 45360 → 871 → 45361 (→ 871)
        540 → 145 (→ 145)

    Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a
    starting number below one million is sixty terms.

    How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

from time import perf_counter
start = perf_counter()

import math


def factorial_digits_sum(num: int) -> int:
    return sum([math.factorial(x) for x in map(int, list(str(num)))])


def get_bound_digit_length() -> int:
    digit_length, max_value = 1, 0
    while digit_length + 1 <= len(str(math.factorial(9) * digit_length)):
        max_value = math.factorial(9) * digit_length
        digit_length += 1
    return max_value


def count_digit_factorial_chain(bound: int, fact_digits_sum: dict) -> None:
    non_repeat_chain_60 = 0
    for start_number in range(bound):
        chain, chain_length = [start_number], 1
        while True:
            chain.append(fact_digits_sum[chain[chain_length-1]])
            if chain[-1] in chain[:-1]:
                if chain_length == 60:
                    non_repeat_chain_60 += 1
                break
            chain_length += 1
    print(non_repeat_chain_60)


def main():

    fact_digits_sum_dict = {i: factorial_digits_sum(i) for i in range(get_bound_digit_length() + 1)}
    count_digit_factorial_chain(1000000, fact_digits_sum_dict)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# 402
# Runtime of the program is 18.2507289000
