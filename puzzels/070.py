""" Totient permutation

    Problem 70
    Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of
    positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7,
    and 8, are all less than nine and relatively prime to nine, φ(9)=6.
    The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

    Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

    Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""

from time import perf_counter
start = perf_counter()

# https://en.wikipedia.org/wiki/Euler%27s_totient_function This solution was checked but not proven correctly.
# we maximize φ(n) if it contains a small amount of large primes, actually we prevent small prime factors
# We have that p/φ(p) = p/p-1 for p = prime but this cannot be a permutation of p so n cannot be prime.
# this became a proof by trial: first check some numbers which are a product of two primes for large enough n.

from lib.library import get_list_of_primes


def totient_function(n: int) -> int:
    result = n
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            while n % i == 0:
                n = n / i
            result = result - result / i
    if n > 1:
        result = result - result / n
    return int(result)


def totient_permutation_minimum_ratio(bound: int) -> None:
    primes, ratio, i, solution = [x for x in get_list_of_primes(4000) if x > 1000], 99, 0, 0
    for p1 in primes:
        i += 1
        for p2 in primes[i:]:
            candidate = int(p1 * p2)
            if candidate > bound:
                break
            totient = totient_function(candidate)
            if sorted(str(candidate)) == sorted(str(totient)):
                if candidate / float(totient) < ratio:
                    ratio, solution = candidate / float(totient), candidate
    print(ratio, solution, totient_function(solution))


totient_permutation_minimum_ratio(10 ** 7)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 1.0007090511248113 8319823 8313928
# Runtime of the program is 9.9278119000

