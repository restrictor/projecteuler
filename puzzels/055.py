""" Lychrel numbers

    Problem 55
    If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

    Not all numbers produce palindromes so quickly. For example,

        349 + 943 = 1292,
        1292 + 2921 = 4213
        4213 + 3124 = 7337

    That is, 349 took three iterations to arrive at a palindrome.

    Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
    A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
    Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that
    a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand,
    it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing
    power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown
    to require over fifty iterations before producing a palindrome: 4668731596684224866951378664
    (53 iterations, 28-digits).

    Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

    How many Lychrel numbers are there below ten-thousand?

    NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
"""

from time import perf_counter
start = perf_counter()


def is_palindromic(number: int) -> bool:
    return str(number) == str(number)[::-1]


def n_lychrel_numbers(n_bound: int, length: int) -> None:
    lychrel_numbers_count = 0
    for number in range(n_bound):
        next_sum, is_lychrel = number + int(str(number)[::-1]), True
        for iteration in range(length):
            if is_palindromic(next_sum):
                is_lychrel = False
                break
            next_sum = next_sum + int(str(next_sum)[::-1])
        if is_lychrel:
            lychrel_numbers_count += 1
    print(lychrel_numbers_count)


n_lychrel_numbers(10000, 50)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 249
# Runtime of the program is 0.0377186000
