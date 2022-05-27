""" Prime power triples

    Problem 87
    The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact,
    there are exactly four numbers below fifty that can be expressed in such a way:

        28 = 2^2 + 2^3 + 2^4
        33 = 3^2 + 2^3 + 2^4
        49 = 5^2 + 2^3 + 2^4
        47 = 2^2 + 3^3 + 2^4

    How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime
    fourth power?
"""

from time import perf_counter
start = perf_counter()

from lib.library import get_list_of_primes


def n_sum_of_powers(pr: list, bound: int) -> None:
    unique_n_sum_of_powers = {}
    second_powers = [x ** 2 for x in pr]
    third_powers = [x ** 3 for x in pr if x ** 3 < bound]
    fourth_powers = [x ** 4 for x in pr if x ** 4 < bound]
    total_numbers = 0

    for second_power in second_powers:
        for third_power in [x for x in third_powers if second_power + x < bound]:
            for fourth_power in [x for x in fourth_powers if second_power + third_power + x < bound]:
                unique_n_sum_of_powers[str(second_power + third_power + fourth_power)] = True
                total_numbers += 1
    print(len(unique_n_sum_of_powers))


def main():

    bound = 50000000
    primes = get_list_of_primes(int(bound ** 0.5))
    n_sum_of_powers(primes, bound)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# 1097343
# Runtime of the program is 0.4090961000