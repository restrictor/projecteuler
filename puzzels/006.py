""" Sum square difference

Problem 6
    The sum of the squares of the first ten natural numbers is,
        1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
    3025 - 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from time import perf_counter
start = perf_counter()


class SumSquareDifference:

    def __init__(self, n):
        self.n = n

    def get_difference_sqr_sum_min_sum_sqr(self) -> int:
        sum_sqr = sum([nn ** 2 for nn in range(1, self.n + 1)])
        sqr_sum = (self.n * (self.n + 1) / 2) ** 2
        return int(sqr_sum - sum_sqr)


a = SumSquareDifference(100)
print(a.get_difference_sqr_sum_min_sum_sqr())

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 25164150
# Runtime of the program is 0.0001186000
