""" Pandigital products

Problem 32
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
    or example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
    and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
    pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from time import perf_counter
start = perf_counter()


def sum_pandigital_products(n_bound: int, length: int) -> None:
    pandigital_products = []
    for multiplicand in range(1, n_bound):
        for multiplier in range(1, multiplicand):
            candidate = str(multiplicand) + str(multiplier) + str(multiplicand * multiplier)
            if len(candidate) <= length:
                set_candidate = set(candidate)
                if '0' not in set_candidate and len(set_candidate) == length:
                    if multiplicand * multiplier not in set(pandigital_products):
                        pandigital_products.append(multiplicand * multiplier)
            else:
                break
    print(sum(pandigital_products))


# 3*4567 = 13701 we see that this is larger than the 9 digits
# 2*3456 = 6912 is still in range so the upper is at least 4567
sum_pandigital_products(4567, 9)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 45228
# Runtime of the program is 0.0532144000
