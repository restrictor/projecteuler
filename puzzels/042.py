""" Coded triangle numbers

    Problem 42
    The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its alphabetical position and adding
    these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10.
    If the word value is a triangle number than we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
    common English words, how many are triangle words?
"""

from time import perf_counter
start = perf_counter()


def map_letter_to_number() -> dict:
    result = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in range(len(alphabet)):
        result[alphabet[letter]] = letter + 1
    return result


def get_triangle_numbers(n_bound: int) -> list:
    triangle_numbers = []
    for i in range(1, n_bound):
        triangle_numbers.append(int(0.5 * i * (i + 1)))
    return triangle_numbers


def count_triangle_words(n_bound: int) -> None:
    triangle_numbers = get_triangle_numbers(n_bound)
    letter_to_number = map_letter_to_number()
    input_data = sorted(open('../data/042.txt').read().rstrip().replace('"', '').split(','))
    triangle_words_count = 0
    for word in input_data:
        character_sum = 0
        for letter in word:
            character_sum += letter_to_number[letter]
        if character_sum in triangle_numbers:
            triangle_words_count += 1
    print(triangle_words_count)


count_triangle_words(1000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 162
# Runtime of the program is 0.0136356000
