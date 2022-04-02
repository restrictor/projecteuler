""" Coin partitions

    Problem 78
    Let p(n) represent the number of different ways in which n coins can be separated into piles.
    For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

        OOOOO
        OOOO   O
        OOO   OO
        OOO   O   O
        OO   OO   O
        OO   O   O   O
        O   O   O   O   O

    Find the least value of n for which p(n) is divisible by one million.
"""

from time import perf_counter
start = perf_counter()

# https://en.wikipedia.org/wiki/Partition_function_(number_theory)
# https://en.wikipedia.org/wiki/Pentagonal_number_theorem


def pentagonal(n: int) -> int:
    return int(n * (3 * n - 1) / 2)


def n_partitions(n_partitions_min_1: list, n: int, pentagonals_list: list) -> int:
    result, index, sign = 0, 0, -1
    while pentagonals_list[index] <= n:
        result += (sign ** index) * n_partitions_min_1[n - pentagonals_list[index]]
        if n >= pentagonals_list[index] + index + 1:
            result += (sign ** index) * n_partitions_min_1[n - (pentagonals_list[index] + index + 1)]
        else:
            return result
        index += 1
    return result


def n_partitions_divisible(divisible_by: int, pentagonal_list_bound: int) -> None:
    pentagonals, n_partitions_list, i = [pentagonal(i) for i in range(1, pentagonal_list_bound)], [1], 1
    while True:
        n_partitions_list.append(n_partitions(n_partitions_list, i, pentagonals))
        if n_partitions_list[-1] % divisible_by == 0:
            print(i)
            break
        i += 1


n_partitions_divisible(1000000, 1000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 55374
# Runtime of the program is 5.2983240000
