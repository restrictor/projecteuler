""" Summation of primes

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from time import perf_counter
start = perf_counter()

# solution for problem 007
from lib.library import get_list_of_primes

print(sum(get_list_of_primes(2000000)))

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 142913828922
# Runtime of the program is 0.0916484000
