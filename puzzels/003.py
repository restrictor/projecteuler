""" Largest prime factor

    Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""

from time import perf_counter
start = perf_counter()


class PrimeFactors:

    def __init__(self, n: int):
        self.n = n
        self.prime_factors = []

    @staticmethod
    def is_prime(number: int) -> bool:
        if number < 2 or number % 2 == 0:
            return False
        elif number == 2:
            return True
        for num in range(3, int(number ** 0.5), 2):
            if number % num == 0:
                return False
        return True

    def get_prime_factors(self) -> None:
        total, i = 1, 2
        while total < self.n:

            # check if i divides n
            if self.n % i == 0:

                # add prime factor and update total factors multiplied
                if self.is_prime(i):
                    self.prime_factors.append(i)
                    total *= i
            i += 1

    def return_largest_prime(self) -> int:
        return self.prime_factors[-1]


a = PrimeFactors(600851475143)
a.get_prime_factors()
print(a.return_largest_prime())
print(a.prime_factors)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 6857
# [71, 839, 1471, 6857]
# Runtime of the program is 0.0019293000
