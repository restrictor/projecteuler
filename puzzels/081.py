""" Path sum: two ways

    Problem 81
    In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right
    and down, is indicated in bold red and is equal to 2427.

    131 673 234 103  18
    201  96 342 965 150
    630 803 746 422 111
    537 699 497 121 956
    805 732 524  37 331

    (red path -> 121 201 96 342 746 422 121 37 331)

    Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt
    (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

from time import perf_counter
start = perf_counter()

from csv import reader
from numpy import array


def import_matrix() -> array:
    with open("../data/081.txt", 'r') as temp:
        result = array([list(map(int, x)) for x in reader(temp, delimiter=',')])
    return result


def get_shortest_path(mat: array) -> None:
    mat[0] = [sum(mat[0][0:i + 1]) for i in range(len(mat))]
    mat[:, 0] = [sum(mat[0:i + 1, 0]) for i in range(len(mat))]
    for i in range(1, len(mat)):
        for j in range(1, len(mat)):
            mat[i][j] = min(mat[i][j] + mat[i - 1, j], mat[i][j] + mat[i, j - 1])
    print(mat[-1, -1])


def main():

    mat = import_matrix()
    get_shortest_path(mat)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# 427337
# Runtime of the program is 0.0971405000
