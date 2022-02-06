""" Longest Collatz sequence

    Problem 14
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting
    numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# get a timer in place
from time import perf_counter
start = perf_counter()


def longest_collatz_sequence(num: int) -> None:
    a = [0] * num
    a[0], a[1], a[2], m = 0, 1, 2, -1
    for i in range(3,num):
        n, j = i, 0
        while n != 1:
            j += 1
            if n % 2 == 0:
                n = int(n / 2)
            else:
                n = int(3 * n + 1)
            if n < i and n != 1:
                a[i], n = j + a[int(n)], 1
        if a[i] == 0:
            a[i] = j
        if a[i] > m:
            m = a[i]
    print(m)


longest_collatz_sequence(1000000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 525
# Runtime of the program is 1.7992973000
