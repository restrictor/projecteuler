""" Passcode derivation

    Problem 79
    A common security method used for online banking is to ask the user for three random characters from a passcode.
    For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected
    reply would be: 317.

    The text file, keylog.txt, contains fifty successful login attempts.

    Given that the three characters are always asked for in order, analyse the file so as to determine the
    shortest possible secret passcode of unknown length.
"""

from time import perf_counter
start = perf_counter()

# this solution works if all values are unique in the passcode


def import_data() -> list:
    random_characters = []
    with open('../data/079.txt', 'r') as f:
        for num in f:
            random_characters.append(int(num))
    return random_characters


def get_ordered_dict(random_characters_list: list) -> dict:
    result = {}
    for i in random_characters_list:
        random_characters_string = str(i)

        # 0->1, 0->2 and 1->2
        for pairs in [[0, 1], [0, 2], [1, 2]]:
            if random_characters_string[pairs[0]] in result.keys():
                if random_characters_string[pairs[1]] not in result[random_characters_string[pairs[0]]]:
                    result[random_characters_string[pairs[0]]].append(random_characters_string[pairs[1]])
            else:
                result[random_characters_string[pairs[0]]] = [random_characters_string[pairs[1]]]
    return result


def is_following(n: int, order_dict: dict) -> bool:
    for followers in order_dict.values():
        if n in followers:
            return True
    return False


def get_secret_password(ordered_dict: dict) -> None:
    unique_digits = list(set([j for sub in ordered_dict.values() for j in sub]))

    # search for numbers that to not follow others (and remove them from the order list)
    shortest_possible_secret_password = []
    while len(ordered_dict) > 0:
        for preceding in list(ordered_dict.keys()):
            if not is_following(preceding, ordered_dict):
                shortest_possible_secret_password.append(preceding)
                del ordered_dict[preceding]

    # add the remaining number(s)
    shortest_possible_secret_password += list(set(unique_digits) - set(shortest_possible_secret_password))
    print(shortest_possible_secret_password)


def main():

    random_characters = import_data()
    ordered_dict = get_ordered_dict(random_characters)
    get_secret_password(ordered_dict)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()


# ['7', '3', '1', '6', '2', '8', '9', '0']
# Runtime of the program is 0.0001766000

