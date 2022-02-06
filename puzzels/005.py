""" Smallest multiple

    Problem 5
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from time import perf_counter
start = perf_counter()


class SmallestMultiple:

    def __init__(self, n):
        self.factors = [1]
        self.total = 1
        self.answer = 1
        self.n = n

    def upper_bound_factors(self) -> None:
        for factor in range(1, self.n + 1):
            if self.total % factor != 0:
                self.total *= factor
                self.factors.append(factor)

    def lower_bound_factors(self) -> None:
        for factor in range(self.n + 1, 1, -1):
            can_remove = 1
            for other_factors in range(1, self.n + 1):
                if (self.total / factor) % other_factors != 0:
                    can_remove = 0
            if can_remove == 1:
                self.total = self.total / factor
                if factor in self.factors:
                    self.factors.remove(factor)

    def get_smallest_multiple(self) -> int:
        self.upper_bound_factors()
        self.lower_bound_factors()
        for factor in self.factors:
            self.answer *= factor
        return self.answer


a = SmallestMultiple(20)
print(a.get_smallest_multiple())

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 2793510720
# Runtime of the program is 0.0001752000