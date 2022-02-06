""" Reciprocal cycles

    Problem 26
    A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
    denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has
    a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from time import perf_counter
start = perf_counter()


def recurring_cycle_length(n: int) -> int:
    route, remainder, digit_i = [0]*n, 1, 0

    # r[remainder] records if (and when) you have been there before. If remainder is 0 it's the end of sequence
    while route[remainder] == 0 and remainder != 0:
        route[remainder] = digit_i
        remainder *= 10
        remainder %= n
        digit_i += 1

    # length digits until it repeats minus the start digit index of the repeating pattern (p)
    return digit_i - route[remainder]


def longest_reciprocal_cycles(n: int) -> None:
    max_recurring_cycle_length = 0
    for i in range(2, n):
        new_cycle_length = recurring_cycle_length(i)
        if new_cycle_length > max_recurring_cycle_length:
            max_recurring_cycle_length = new_cycle_length
    print(max_recurring_cycle_length)


longest_reciprocal_cycles(1000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 982
# Runtime of the program is 0.0254979000
