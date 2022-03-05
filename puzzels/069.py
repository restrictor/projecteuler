""" Totient maximum

Problem 69
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number
of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, φ(9)=6.

    n 	Relatively Prime 	φ(n) 	n/φ(n)
    2 	1 	                1 	    2
    3 	1,2 	            2 	    1.5
    4 	1,3 	            2 	    2
    5 	1,2,3,4 	        4 	    1.25
    6 	1,5 	            2 	    3
    7 	1,2,3,4,5,6 	    6 	    1.1666...
    8 	1,3,5,7 	        4 	    2
    9 	1,2,4,5,7,8 	    6 	    1.5
    10 	1,3,7,9 	        4 	    2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

from time import perf_counter
start = perf_counter()

# for clues, we thank Euler for his product formula φ(n) = n II_p|n (1-1/p) for distinct primes.
# n/φ(n) is maximized if n contains relatively many prime factors. Can you see why that is so?
# see for more information the source: https://en.wikipedia.org/wiki/Euler%27s_totient_function
# Also notice that the divisor sum established by Gauss states that ∑ φ(d) = n for divisors(n).

# solution for problem 007
from lib.library import get_list_of_primes


def totient_max_value(bound: int, primes: list) -> int:
    max_n_value, i = 1, 0
    while max_n_value * primes[i] < bound:
        max_n_value *= primes[i]
        i += 1
    return max_n_value


print(totient_max_value(1000000, get_list_of_primes(30)))

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 510510
# Runtime of the program is 0.0074990000
