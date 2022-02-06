""" Number letter counts

    Problem 17
    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342
    (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
    contains 20 letters. The use of "and" when writing out numbers
    is in compliance with British usage.


"""

from time import perf_counter
start = perf_counter()

import inflect


def number_letter_counts(n: int) -> int:
    p = inflect.engine()
    return sum(len(p.number_to_words(i).replace("-", "").replace(" ", "")) for i in range(1, n + 1))


print(number_letter_counts(1000))

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 21124
# Runtime of the program is 0.0328688000
