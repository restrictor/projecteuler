""" Path sum: three ways

    Problem 82
    NOTE: This problem is a more challenging version of Problem 81.

    The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any
    cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

        131 673 234 103  18
        201  96 342 965 150
        630 803 746 422 111
        537 699 497 121 956
        805 732 524  37 331

        (red path -> 201 96 342 234 103 18)

    Find the minimal path sum from the left column to the right column in matrix.txt
    (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

from time import perf_counter
start = perf_counter()

from csv import reader
from numpy import array


def import_matrix() -> array:
    with open("../data/082.txt", 'r') as temp:
        result = array([list(map(int, x)) for x in reader(temp, delimiter=',')])
    return result


def get_shortest_path(mat: array) -> None:
    mat[:, 1] = mat[:, 1] + mat[:, 0]
    for column in range(2, len(mat)):

        # list per column with new values
        column_values = []
        for row in range(len(mat)):
            move_up, move_down = 10 ** 10, 10 ** 10

            # above
            for k in range(row + 1):
                if sum(mat[k:row + 1, column]) + mat[k, column - 1] < move_up:
                    move_up = sum(mat[k:row + 1, column]) + mat[k, column - 1]

            # below
            for k in range(row, len(mat)):
                if sum(mat[row:k + 1, column]) + mat[k, column - 1] < move_down:
                    move_down = sum(mat[row:k + 1, column]) + mat[k, column - 1]

            column_values.append(min(min(mat[row][column] + mat[row, column - 1], move_up), move_down))
        mat[:, column] = column_values
    print(min(mat[:, len(mat) - 1]))


def main():

    mat = import_matrix()
    get_shortest_path(mat)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# 260324
# Runtime of the program is 1.7212649000
