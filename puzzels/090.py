""" Cube digit pairs

    Problem 90
    Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second
    cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

    For example, the square number 64 could be formed:

                                      ,════════════════════╦µ «════════════════════▄
                                    ¿"                   ,▒░▌                    √▒▐
                                  ¿`                   ╓▒░╝                    m░▒▒▐
                                g▄,,,,,,,,,,,,,,,,,,,╔▒░▓,,,,,,,,,,,,,,,,,,,╓Φ░▒▒▒▒▐
                                                     ▌▒▓                    ╠▒▒▒▒▒▒▐
                                C       ▄████L       ▌▒▓          ▄▄▄       ╠▒▒▒▒▒▒▐
                                C     ▄█▀            ▌▒▓        ▄█▀██       ╠▒▒▒▒▒▒▐
                                      █▌,▄▄▄,        ▌▒▓      ╓█▀  ██       ╠▒▒▒▒▒▒▐
                                C    ▐█▀`''`██       ▌▒▓     ██▄,,▄██,      ╠▒▒▒▒▒▒▐
                                C     █▌     █▌      ▌▒▓     ▀▀▀▀▀▀██▀      ╠▒▒▒▒▒▒▐
                                C     ▀█▄  ,██       ▌▒▓           ██       ╠▒▒▒▒░▒`
                                C       ▀▀▀▀`        ▌▒▓           ▀▀       ╠▒▒░╨`
                                C                    ▌▒▓                    ╠░╝
                                ════════════════════╦µ «════════════════════

    In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below
    one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

    For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on
    the other cube.

    However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like
    {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would
    be impossible to obtain 09.

    In determining a distinct arrangement we are interested in the digits on each cube, not the order.

        {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
        {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

    But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the
    extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

    How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
"""

from time import perf_counter
start = perf_counter()

import itertools


def count_distinct_arrangements(numbers: list, combinations: list) -> None:
    unique_solution = {}
    for i in range(len(combinations)):
        cube1 = combinations[i]
        for j in range(len(combinations)):
            cube2 = combinations[j]
            if i > j:
                if 6 in cube1:
                    cube1_candidate = cube1 + [9]
                elif 9 in cube1:
                    cube1_candidate = cube1 + [6]
                else:
                    cube1_candidate = cube1

                if 6 in cube2:
                    cube2_candidate = cube2 + [9]
                elif 9 in cube2:
                    cube2_candidate = cube2 + [6]
                else:
                    cube2_candidate = cube2
                fail = False

                for square in numbers:
                    in_cube1 = int(square[0]) in cube1_candidate
                    in_cube2 = int(square[1]) in cube2_candidate

                    in_cube1_rev = int(square[1]) in cube1_candidate
                    in_cube2_rev = int(square[0]) in cube2_candidate
                    if (in_cube1 and in_cube2) or (in_cube1_rev and in_cube2_rev):
                        pass
                    else:
                        fail = True
                        break
                if not fail:
                    if str(sorted(cube1)) + "-" + str(sorted(cube2)) not in unique_solution:
                        unique_solution[str(sorted(cube1)) + "-" + str(sorted(cube2))] = True
    print(len(unique_solution))


def main():

    nine_sq = [('0' + str(i * i))[-2:] for i in range(1, 10)]
    comb = [list(x) for x in list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6))]
    count_distinct_arrangements(nine_sq, comb)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# 1217
# Runtime of the program is 0.0409939000