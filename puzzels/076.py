""" Counting summations

    Problem 76
    It is possible to write five as a sum in exactly six different ways:

        4 + 1
        3 + 2
        3 + 1 + 1
        2 + 2 + 1
        2 + 1 + 1 + 1
        1 + 1 + 1 + 1 + 1

    How many different ways can one hundred be written as a sum of at least two positive integers?
"""
from time import perf_counter
start = perf_counter()

# solution for problem 031
from lib.library import times_to_make_a_number


def main():

    amount = 100
    coins_list = list(range(1, amount))
    print(times_to_make_a_number(coins_list, amount))

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# 190569291
# Runtime of the program is 0.0008747000
