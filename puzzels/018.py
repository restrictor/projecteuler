""" Maximum path sum I

    Problem 18
    By starting at the top of the triangle below and moving to adjacent numbers on the row below,
    the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

                            75
                          95 64
                        17 47 82
                       18 35 87 10
                     20 04 82 47 65
                    19 01 23 75 03 34
                   88 02 77 73 07 63 67
                 99 65 04 28 06 16 70 92
               41 41 26 56 83 40 80 70 33
             41 48 72 33 47 32 37 16 94 29
           53 71 44 65 25 43 91 52 97 51 14
         70 11 33 28 77 73 17 78 39 68 17 57
       91 71 52 38 17 14 91 43 58 50 27 29 48
     63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem by
    trying every route. However, Problem 67, is the same challenge with a triangle
    containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

from time import perf_counter
start = perf_counter()


def print_triangle() -> None:
    for i in range(len(triangle)):
        print("{: ^70s}".format(str(triangle[i])))


def read_triangle() -> list:
    tri = []
    with open('../data/018.txt', 'r') as f:
        for num in f:
            tri.append([int(x) for x in num.rstrip().split()])
    return tri


def maximum_path_sum(tri: list) -> list:
    # iterate over the columns
    for y in range((len(tri) - 2), -1, -1):

        # iterate over the rows
        for x in range(len(tri[y])):
            tri[y][x] += max(tri[y + 1][x], tri[y + 1][x + 1])
    return tri


triangle = read_triangle()
print_triangle()
triangle = maximum_path_sum(triangle)
print(triangle[0][0])
print_triangle()

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")
#
#                                  [75]
#                                [95, 64]
#                              [17, 47, 82]
#                            [18, 35, 87, 10]
#                          [20, 4, 82, 47, 65]
#                         [19, 1, 23, 75, 3, 34]
#                       [88, 2, 77, 73, 7, 63, 67]
#                     [99, 65, 4, 28, 6, 16, 70, 92]
#                  [41, 41, 26, 56, 83, 40, 80, 70, 33]
#                [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
#              [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
#            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
#          [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
#        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
#       [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
# 1074
#                                 [1074]
#                               [995, 999]
#                            [818, 900, 935]
#                          [704, 801, 853, 792]
#                       [686, 640, 766, 731, 782]
#                     [666, 614, 636, 684, 660, 717]
#                  [647, 501, 613, 609, 533, 657, 683]
#                [559, 499, 479, 536, 514, 526, 594, 616]
#             [460, 434, 419, 475, 508, 470, 510, 524, 487]
#           [419, 365, 393, 387, 419, 425, 430, 376, 454, 322]
#        [378, 317, 231, 321, 354, 372, 393, 354, 360, 293, 247]
#      [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233]
#   [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148]
#  [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54]
#       [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
# Runtime of the program is 0.0003405000
#
# Process finished with exit code 0

