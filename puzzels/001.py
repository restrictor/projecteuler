""" Multiples of 3 or 5

    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""

from time import perf_counter
start = perf_counter()


class MultiplesOf35:

    def __init__(self, n):
        self.n = n
        self.multiples = [i for i in range(n) if i % 3 == 0 or i % 5 == 0]

    def calculate_sum_multiples(self) -> int:
        return sum(self.multiples)


a = MultiplesOf35(1000)
print(a.calculate_sum_multiples())
end = perf_counter()

print(f"Runtime of the program is {end - start:.10f}")

# 233168
# Runtime of the program is 0.0001801000
