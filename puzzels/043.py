""" Sub-string divisibility

    Problem 43
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the
    digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17
    Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from time import perf_counter
start = perf_counter()

from itertools import permutations


def concat_divisibles(front: list, back: list) -> list:
    solution = []
    for back_digits in back:
        for front_digits in front:
            if front_digits[1:] == back_digits[0:2]:
                if front_digits[0] not in back_digits:
                    solution.append(front_digits[0] + back_digits)
    return solution


def pandigital_sub_string_divisibility() -> None:
    digits = "0123456789"
    primes = [2, 3, 5, 7, 11, 13, 17]
    three_digits = ["".join(x) for x in list(permutations(digits, 3))]
    divisible = [[x for x in three_digits if int(x) % y == 0] for y in primes]

    connect_13_17 = concat_divisibles(divisible[-2], divisible[-1])
    connect_11_13_17 = concat_divisibles(divisible[-3], connect_13_17)
    connect_7_11_13_17 = concat_divisibles(divisible[-4], connect_11_13_17)
    connect_5_7_11_13_17 = concat_divisibles(divisible[-5], connect_7_11_13_17)
    connect_3_5_7_11_13_17 = concat_divisibles(divisible[-6], connect_5_7_11_13_17)
    connect_2_3_5_7_11_13_17 = concat_divisibles(divisible[-7], connect_3_5_7_11_13_17)
    connect_1_2_3_5_7_11_13_17 = [list(set(digits) - set(x))[0] + x for x in connect_2_3_5_7_11_13_17]
    print(sum([int(x) for x in connect_1_2_3_5_7_11_13_17]))


pandigital_sub_string_divisibility()

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# ['4160357289', '1460357289', '4106357289', '1406357289', '4130952867', '1430952867']
# 16695334890
# Runtime of the program is 0.0036712000
