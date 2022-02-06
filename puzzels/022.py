""" Names scores

    Problem 22
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
    first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth
     3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
"""

from time import perf_counter
start = perf_counter()


def name_score(n: int, name: str, alphabet: dict) -> int:
    name_sum = 0
    for j in range(len(name)):
        name_sum += alphabet[name[j]]
    return n*name_sum


def create_alfa_dict() -> dict:
    alfa_dict = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(alphabet)):
        alfa_dict[alphabet[i]] = i + 1
    return alfa_dict


def score(alpha_dict: dict) -> None:
    input_data = sorted(open('../data/022.txt').read().rstrip().replace('"', '').split(','))
    total_names_score = 0
    for i in range(len(input_data)):
        total_names_score += name_score(i+1, input_data[i], alpha_dict)
    print(total_names_score)


score(create_alfa_dict())

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 871198282
# Runtime of the program is 0.0062718000
