""" 10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from time import perf_counter
start = perf_counter()


class ListOfPrimes:
    """ Returns  a list of primes < n """

    def __init__(self, n):
        self.n = n
        self.primes = []

    def get_list_of_primes(self) -> None:
        """ sieve the non primes out """

        sieve = [True] * self.n
        for i in range(3, int(self.n ** 0.5) + 1, 2):
            if sieve[i]:
                sieve[i * i::2 * i] = [False] * ((self.n - i * i - 1) // (2 * i) + 1)
        self.primes = [2] + [i for i in range(3, self.n, 2) if sieve[i]]


a = ListOfPrimes(120000)
a.get_list_of_primes()
print(a.primes[10000])

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 104743
# Runtime of the program is 0.0055931000
