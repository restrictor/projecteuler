""" Pandigital prime

    Problem 41
    We shall say that an n-digit number is pandigital if it makes use of all the
    digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
"""

from time import perf_counter
start = perf_counter()


def divisible_by_three(digits: list) -> bool:
    return sum(digits) % 3 == 0


def get_candidate_length() -> int:
    for number_of_digits in range(9, 1, -1):
        if not divisible_by_three([j for j in range(1, number_of_digits + 1)]):
            return number_of_digits


# try the limited possibilities
def why_not_more_loops() -> int:
    digits_list = [i for i in range(1, get_candidate_length() + 1)][::-1]
    ii = 0
    for i in digits_list:
        j_set = sorted(list(set(digits_list) - {i}), reverse=True)
        for j in j_set:
            k_set = sorted(list(set(j_set) - {j}), reverse=True)
            for k in k_set:
                l_set = sorted(list(set(k_set) - {k}), reverse=True)
                for l in l_set:
                    m_set = sorted(list(set(l_set) - {l}), reverse=True)
                    for m in m_set:
                        n_set = sorted(list(set(m_set) - {m}), reverse=True)
                        for n in n_set:
                            o_set = sorted(list(set(n_set) - {n}), reverse=True)
                            for o in o_set:
                                s = str(i) + str(j) + str(k) + str(l) + str(m) + str(n) + str(o)
                                ii += 1
                                if is_prime(int(s)):
                                    return int(s)


# solution for problem 003
from lib.library import is_prime
print(why_not_more_loops())

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 7652413
# Runtime of the program is 0.0026467000
