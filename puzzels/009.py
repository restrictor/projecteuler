""" Special Pythagorean triplet

    Problem 9
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 1^6 = 2^5 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

from time import perf_counter


# brute force
def special_pythagorean_triplet(sum_is: int = 1000) -> (int, int, int, int):
    for i in range(1, int(sum_is)):
        for j in range(i + 1, sum_is - i):
            k = sum_is - i - j
            if i ** 2 + j ** 2 == k ** 2:
                return i, j, k, i * j * k


# euclid's method
def euclid_pythagorean_triples(sum_is: int = 1000) -> (int, int, int, int):
    for i in range(1, int(sum_is / 3)):
        for j in range(i + 1, sum_is - i):
            a = 2 * i * j
            b = j ** 2 - i ** 2
            c = i ** 2 + j ** 2
            if a + b + c == sum_is:
                return a, b, c, a * b * c


def main():
    start = perf_counter()
    bound = 1000

    # try euclid (might not work if it is not a primitive)
    triple = euclid_pythagorean_triples(bound)
    print(triple)

    if not triple:
        triple = special_pythagorean_triplet(sum_is=bound)
        print(triple)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# (200, 375, 425, 31875000)
# Runtime of the program is 0.0062277000
