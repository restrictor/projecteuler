""" Product-sum numbers

    Problem 88
    A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers,
    {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

    For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

    For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number.
    The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

        k=2: 4 = 2 × 2 = 2 + 2
        k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
        k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
        k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
        k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

    Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once
    in the sum.

    In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

    What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
"""

# elegant solution is different

from time import perf_counter
start = perf_counter()


def two_factorization(factors: list, number: int) -> list:
    two_factors = []
    for i in range(len(factors) // 2):
        two_factors.append([factors[i], factors[-(i + 1)]])
    if len(two_factors) % 2 != 0 and factors[len(factors) // 2] ** 2 == number:
        two_factors.append([factors[len(factors) // 2], factors[len(factors) // 2]])
    return two_factors


def factors_and_factor_pairs(number: int) -> dict:
    # single factors
    factors, factor_groups = [y for y in range(2, number) if number % y == 0], {}
    if not factors:
        return {}
    factor_groups[1] = factors

    # pairs of factors
    if len(factor_groups[1]) == 1:
        factor_groups[2] = [[factor_groups[1][0], factor_groups[1][0]]]
        return factor_groups
    factor_groups[2] = []
    for i in range(len(factors) // 2):
        factor_groups[2].append([factors[i], factors[-(i + 1)]])
    if len(factor_groups[2]) % 2 != 0 and factors[len(factors) // 2] ** 2 == number:
        factor_groups[2].append([factors[len(factors) // 2], factors[len(factors) // 2]])
    return factor_groups


def factorisations(number: int, maximum_number_of_factors: int) -> dict:
    pairs = factors_and_factor_pairs(number)
    if pairs == {}:
        return {}

    for n_factor in range(3, maximum_number_of_factors + 1):
        pairs[n_factor] = []
        for n_fact in pairs[n_factor - 1]:
            for index in range(len(n_fact)):
                factor_a = n_fact[index]
                divisors = [div for div in range(2, factor_a) if factor_a % div == 0]
                if divisors:
                    factors = two_factorization(divisors, factor_a)
                    if not factors:
                        if sorted(divisors + divisors + n_fact[:index] + n_fact[index + 1:]) not in pairs[n_factor]:
                            pairs[n_factor].append(divisors + divisors + n_fact[:index] + n_fact[index + 1:])
                    else:
                        for fac in factors:
                            if sorted(fac + n_fact[:index] + n_fact[index + 1:]) not in pairs[n_factor]:
                                pairs[n_factor].append(sorted(fac + n_fact[:index] + n_fact[index + 1:]))
            if not pairs[n_factor]:
                pairs.pop(n_factor)
                return pairs
    return pairs


def factorisations_dict(depth: int, k: int) -> (dict, dict):
    f_dict, s_dict = {}, {}
    for i in range(2, 2 * (k + 2)):
        f_dict[i] = factorisations(i, depth)
        if i < k + 1:
            s_dict[i] = 10000000
        if f_dict[i] != {}:
            f_dict[i][1] = [f_dict[i][1]]
    return f_dict, s_dict


def minimal_product_sum(d: dict, s: dict, k: int) -> None:
    for i in range(2, k + 1):
        found = False

        # possible candidates
        for j in range(i + 2, 2 * (i + 2)):
            if s[i] == 10000000 and found is False:

                # check if j is solution
                if d[j] != {} and found is False:
                    for it, v in d[j].items():
                        for vv in v:
                            if i - it + sum(vv) == j and it != 1:
                                s[i], found = j, True
                                break
            else:
                break
    tot = []
    for kk, vv in s.items():
        if vv not in tot:
            tot.append(vv)
    print(sum(tot))


def main():

    k = 12000
    factors_dict, score_dict = factorisations_dict(30, k)
    minimal_product_sum(factors_dict, score_dict, k)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# 7587457
# Runtime of the program is 25.2418956000
