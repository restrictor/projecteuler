""" Pandigital multiples

    Problem 38
    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576
    the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving
    the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
    product of an integer with (1,2, ... , n) where n > 1?
"""

from time import perf_counter
start = perf_counter()


def is_pandigital(n: int, i: int) -> (bool, str):
    c = "".join([str(j * n) for j in range(1, i + 1)])
    return sorted(list(c)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9'], c


def pandigital_concatenated_product() -> None:
    max_pandigital_concatenated_product = 0
    for number in range(10000):
        for integer in range(10):
            candidate = is_pandigital(number, integer)
            if candidate[0] and max_pandigital_concatenated_product < int(candidate[1]):
                max_pandigital_concatenated_product = int(candidate[1])
    print(max_pandigital_concatenated_product)


pandigital_concatenated_product()

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 932718654
# Runtime of the program is 0.2801510000
