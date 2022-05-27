""" Cuboid route

    Problem 86
    A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner.
    By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is
    shown on the diagram.
                                                                        F
                             --------------------------------------
                           / #                                 * / #
                          /  #                               *  /  #
                         /   #                              *  /   #    3
                        /    #                             *  /    #
                       /     #                           *   /     #
                      #------#-------------------------*---#       #
                      #      #                       *     #       #
                      #      #---------------------*-------#------/
                      #     /                   **         #     /
                      #    /              **               #    /
                      #   /         **                     #   /    5
                      #  /     **                          #  /
                      # /  **                              # /
                      #/-----------------------------------#/
                  S                     6

    However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't
    always have integer length.

    It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up
    to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the
    least value of M for which the number of solutions first exceeds two thousand; the number of solutions when
    M = 99 is 1975.

    Find the least value of M such that the number of solutions first exceeds one million.
"""

from time import perf_counter
start = perf_counter()


# notice that we are looking for pythagorean triples
from lib.library import primitive_triples


def number_of_cuboids(a: int, b_plus_c: int) -> int:
    if 2 * a < b_plus_c:
        return 0
    elif a >= b_plus_c:
        return b_plus_c // 2
    else:
        if b_plus_c % 2 == 0:
            return a + 1 - (b_plus_c // 2)
        else:
            return a - ((b_plus_c - 1) // 2)


def find_solution(primitives: list, bound: int) -> None:
    maximum_side_length = 10000
    triples = [0] * maximum_side_length * 10
    for triple_sorted in primitives:
        b = triple_sorted[1]
        c = triple_sorted[2]
        for k in range(1, int(maximum_side_length / b) + 1):
            triples[k * b] += number_of_cuboids(k * b, k * c)
        for k in range(1, int(maximum_side_length / c) + 1):
            triples[k * c] += number_of_cuboids(k * c, k * b)

    combination_count = 0
    for M in range(len(triples)):
        combination_count += triples[M]
        if combination_count > bound:
            print(M)
            break


def main():

    sorted_primitives = [sorted(triple)[::-1] for triple in [[3, 4, 5]] + primitive_triples(3, 4, 5, 10000)]
    find_solution(sorted_primitives, 1000000)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# 1818
# Runtime of the program is 0.0399943000
