""" Largest palindrome product

    Problem 4
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
    numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""

# either XYZZYY or XYZYX for 5 or 6 length palindromes
# so there are only 9*10*10 for 5 and 6 length
# and all even length palindromes are dividable by 11, why?

from time import perf_counter
start = perf_counter()


class Largest6Palindrome:

    def __init__(self):
        self.palindromes = []

    def get_6_palindromes(self) -> None:
        for i in range(9, 0, -1):
            for j in range(9, -1, -1):
                for k in range(9, -1, -1):
                    self.palindromes.append(str(i) + str(j) + str(k) + str(k) + str(j) + str(i))

    def get_largest_palindrome(self) -> str:
        for p in self.palindromes:
            for k in range(99, 999, 11):
                if int(p) % k == 0 and int(p)/k < 999:
                    return p


a = Largest6Palindrome()
a.get_6_palindromes()
print(a.palindromes[0:10])
print(a.get_largest_palindrome())

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# ['999999', '998899', '997799', '996699', '995599', '994499', '993399', '992299', '991199', '990099']
# 906609
# Runtime of the program is 0.0028291000