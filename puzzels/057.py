""" Square root convergents

    Problem 57
    It is possible to show that the square root of two can be expressed as an infinite continued fraction.

        2–√=1+1/(2+1/(2+1/(2+…)))

    By expanding this for the first four iterations, we get:

        1+1/2=3/2=1.5

        1+1/(2+1/2)=7/5=1.4
        1+1/(2+1/(2+1/2))=17/12=1.41666...
        1+1/(2+1/(2+1/(2+1/2)))=41/29=1.41379...

    The next three expansions are 99/70 , 239/169, and 577/408, but the eighth expansion, 1393/985,
    is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

    In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""

from time import perf_counter
start = perf_counter()

# Let p/q convergent -> 1 + 1/(1+p/q) = 1 + q/(p+q) = (p+2q)/p+q so p_n+1 -> p_n + 2q_n and q_n+1 -> p_n + q_n


def next_square_convergent(p, q):
    return p + 2*q, p + q


def count_numerator_more_digits_denominator(n_bound):
    p, q, total = 1, 1, 0
    for i in range(n_bound):
        p, q = next_square_convergent(p, q)
        if len(str(p)) > len(str(q)):
            total += 1
    print(total)


count_numerator_more_digits_denominator(1000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 153
# Runtime of the program is 0.0028514000
