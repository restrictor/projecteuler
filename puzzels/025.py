""" 1000-digit Fibonacci number

    Problem 25
    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

from time import perf_counter
start = perf_counter()


def next_fi(n1: int, n2: int) -> (int, int):
    return n2, n1 + n2


def fibonacci_n_digit_number(num: int) -> None:
    nn1, nn2, i = 1, 1, 0
    while 1:
        nn1, nn2 = next_fi(nn1, nn2)
        if len(str(nn2)) >= num:
            print(i+3)
            break
        i += 1


fibonacci_n_digit_number(1000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 4782
# Runtime of the program is 0.0306797000
