""" Singular integer right triangles

    Problem 75
    It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right
    angle triangle in exactly one way, but there are many more examples.

        12 cm: (3,4,5)
        24 cm: (6,8,10)
        30 cm: (5,12,13)
        36 cm: (9,12,15)
        40 cm: (8,15,17)
        48 cm: (12,16,20)

    In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle,
    and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form
    exactly three different integer sided right angle triangles.

        120 cm: (30,40,50), (20,48,52), (24,45,51)

    Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided
    right angle triangle be formed?
"""

from time import perf_counter
start = perf_counter()

# triples: https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
# generate all triples with n and only count when one member


def primitive_triples(x: int, y: int, z: int, cir: int = 12) -> list:

    x1 = -x + 2 * y + 2 * z
    y1 = -2 * x + y + 2 * z
    z1 = -2 * x + 2 * y + 3 * z

    x2 = x + 2 * y + 2 * z
    y2 = 2 * x + y + 2 * z
    z2 = 2 * x + 2 * y + 3 * z

    x3 = x - 2 * y + 2 * z
    y3 = 2 * x - y + 2 * z
    z3 = 2 * x - 2 * y + 3 * z

    if x1 + y1 + z1 > cir and x2 + y2 + z2 > cir and x3 + y3 + z3 > cir:
        return []
    if x1 + y1 + z1 > cir and x2 + y2 + z2 > cir:
        return [[x3, y3, z3]] + primitive_triples(x3, y3, z3, cir)
    if x2 + y2 + z2 > cir and x3 + y3 + z3 > cir:
        return [[x1, y1, z1]] + primitive_triples(x1, y1, z1, cir)
    if x1 + y1 + z1 > cir and x3 + y3 + z3 > cir:
        return [[x2, y2, z2]] + primitive_triples(x2, y2, z2, cir)
    if x1 + y1 + z1 > cir:
        return [[x2, y2, z2]] + primitive_triples(x2, y2, z2, cir) + \
               [[x3, y3, z3]] + primitive_triples(x3, y3, z3, cir)
    if x2 + y2 + z2 > cir:
        return [[x1, y1, z1]] + primitive_triples(x1, y1, z1, cir) + \
               [[x3, y3, z3]] + primitive_triples(x3, y3, z3, cir)
    if x3 + y3 + z3 > cir:
        return [[x1, y1, z1]] + primitive_triples(x1, y1, z1, cir) + \
               [[x2, y2, z2]] + primitive_triples(x2, y2, z2, cir)

    return [[x1, y1, z1]] + primitive_triples(x1, y1, z1, cir) + \
           [[x2, y2, z2]] + primitive_triples(x2, y2, z2, cir) + \
           [[x3, y3, z3]] + primitive_triples(x3, y3, z3, cir)


def add_non_primitive_triples(prim_triples: list, bound: int) -> list:
    for t in list(prim_triples):
        i = 2
        while sum(t) * i < bound:
            prim_triples.append([x * i for x in t])
            i += 1
    return prim_triples


def count_singular_integer_right_triangles(triples: list) -> None:
    integer_right_triangles_count = {}
    for triple in triples:
        if sum(triple) in integer_right_triangles_count.keys():
            integer_right_triangles_count[sum(triple)] += 1
        else:
            integer_right_triangles_count[sum(triple)] = 1
    count = 0
    for k, v in integer_right_triangles_count.items():
        if integer_right_triangles_count[k] == 1:
            count += 1
    print(count)


def main():

    bound = 1500000
    primitive = [[3, 4, 5]] + primitive_triples(3, 4, 5, cir=bound)
    integer_right_triangles = add_non_primitive_triples(primitive, bound)
    count_singular_integer_right_triangles(integer_right_triangles)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")

if __name__ == "__main__":
    main()

# 161667
# Runtime of the program is 2.4733352000