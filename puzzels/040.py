""" Champernowne's constant

    Problem 40
    An irrational decimal fraction is created by concatenating the positive integers:

        0.12345678910 1 112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If d_n represents the nth digit of the fractional part, find the value of the following expression.

    d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""

from time import perf_counter
start = perf_counter()


def champernowne_constant(upper: int) -> None:
    s = ""
    for i in range(upper):
        s = s + str(i)
    value = int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])
    print(value)


champernowne_constant(int(1000000/5))

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 210
# Runtime of the program is 0.0585482000
