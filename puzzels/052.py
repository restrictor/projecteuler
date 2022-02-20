""" Permuted multiples

    Problem 52
    It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
    but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from time import perf_counter
start = perf_counter()

# alot of iterations can be skipped because the digit number will change during multiplication
# 2 digits = (1-16), 3 digits = (17-166), 4 digits (167-1666) etc
# so we only need to check for numbers in the list [10-16, 100-166, 1000-1666, etc ]


def smallest_permited_multiples_number() -> None:
    d = 1
    while 1:
        ll = [x for s in [list(range(10 ** j, int(10 ** j + 10 ** j * 2 / 3 + 1))) for j in range(d-1, d)] for x in s]
        for i in ll:
            if sorted(list(str(i))) == sorted(list(str(2*i))):
                if sorted(list(str(i))) == sorted(list(str(3*i))):
                    if sorted(list(str(i))) == sorted(list(str(4*i))):
                        if sorted(list(str(i))) == sorted(list(str(5*i))):
                            if sorted(list(str(i))) == sorted(list(str(6*i))):
                                print(i)
                                return
        d += 1


smallest_permited_multiples_number()

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 142857
# Runtime of the program is 0.0547342000
