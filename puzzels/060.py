""" Prime pair sets

    Problem 60
    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating
    them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and
    1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four
    primes with this property.

    Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

from time import perf_counter
start = perf_counter()

# implementation taken from: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
from lib.library import get_list_of_primes, is_prime_341_trillion as is_prime


def can_pair_with_five(n_bound: int) -> list:
    primes, pairs_with_five = get_list_of_primes(n_bound), []
    pss = primes[:20]
    for candidate_prime in primes:
        pairings, str_can = 0, str(candidate_prime)
        for prime in primes:
            if candidate_prime < prime and pairings < 5:
                str_prime = str(prime)
                if is_prime(int(str_can + str_prime), pss) and is_prime(int(str_prime + str_can), pss):
                    pairings += 1
        if pairings > 4:
            pairs_with_five.append(candidate_prime)
    return pairs_with_five


def lowest_sum_five_pairing_prime(pairs_with_five: list) -> None:
    min_sum, solution, primes = 999999999999999, 0, get_list_of_primes(20)
    for prime_candidate in pairs_with_five:
        can = [prime_candidate]
        for y in pairs_with_five:
            if y < prime_candidate:
                str_y, can_pair_with_each_other = str(y), True
                for x in can:
                    str_x = str(x)
                    if is_prime(int(str_x + str_y), primes) and is_prime(int(str_y + str_x), primes):
                        pass
                    else:
                        can_pair_with_each_other = False
                        break
                if can_pair_with_each_other:
                    can.append(y)
        if len(can) > 4 and sum(sorted(can)[0:5]) < min_sum:
            solution, min_sum = (sorted(can)[0:5]), sum(sorted(can)[0:5])
    print(solution, min_sum)


pairs_5 = can_pair_with_five(10000)
lowest_sum_five_pairing_prime(pairs_5)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# [13, 5197, 5701, 6733, 8389] 26033
# Runtime of the program is 4.1135922000
