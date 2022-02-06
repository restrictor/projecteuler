""" Digit cancelling fractions

    Problem 33
    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify
    it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less than one in value,
    and containing two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from time import perf_counter
start = perf_counter()


def digit_cancelling_fractions() -> None:
    product_numerator, product_denominator = 1, 1
    for i in range(1, 10):
        for j in range(10):
            numerator = i * 10 + j
            for denominator in range(numerator + 1, 100):

                # case first and second digit
                if int(str(denominator)[1]) != 0 and int(str(denominator)[0]) == j:
                    if i / float(str(denominator)[1]) == numerator / denominator:
                        print(str(numerator) + "/" + str(denominator))
                        product_numerator *= numerator
                        product_denominator *= denominator
    print(product_numerator / product_denominator)


digit_cancelling_fractions()

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 16/64
# 19/95
# 26/65
# 49/98
# 0.01
# Runtime of the program is 0.0027767000
