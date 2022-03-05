""" Maximum path sum II

    Problem 67
    By starting at the top of the triangle below and moving to adjacent numbers on the row below,
    the maximum total from top to bottom is 23.

           3
          7 4
         2 4 6
        8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
    a 15K text file containing a triangle with one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to
    solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every
    second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

from time import perf_counter
start = perf_counter()
# from solution 18


def print_triangle() -> None:
    for i in range(min(len(triangle), 20)):
        print("{: ^100s}".format(str(triangle[i])))
    print("....")

def read_triangle() -> list:
    tri = []
    with open('../data/067.txt', 'r') as f:
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

#                                                 [59]
#                                               [73, 41]
#                                             [52, 40, 9]
#                                           [26, 53, 6, 34]
#                                         [10, 51, 87, 86, 81]
#                                       [61, 95, 66, 57, 25, 68]
#                                     [90, 81, 80, 38, 92, 67, 73]
#                                   [30, 28, 51, 76, 81, 18, 75, 44]
#                                 [84, 14, 95, 87, 62, 81, 17, 78, 58]
#                                [21, 46, 71, 58, 2, 79, 62, 39, 31, 9]
#                             [56, 34, 35, 53, 78, 31, 81, 18, 90, 93, 15]
#                           [78, 53, 4, 21, 84, 93, 32, 13, 97, 11, 37, 51]
#                          [45, 3, 81, 79, 5, 18, 78, 86, 13, 30, 63, 99, 95]
#                        [39, 87, 96, 28, 3, 38, 42, 17, 82, 87, 58, 7, 22, 57]
#                       [6, 17, 51, 17, 7, 93, 9, 7, 75, 97, 95, 78, 87, 8, 53]
#                   [67, 66, 59, 60, 88, 99, 94, 65, 55, 77, 55, 34, 27, 53, 78, 28]
#                  [76, 40, 41, 4, 87, 16, 9, 42, 75, 69, 23, 97, 30, 60, 10, 79, 87]
#               [12, 10, 44, 26, 21, 36, 32, 84, 98, 60, 13, 12, 36, 16, 63, 31, 91, 35]
#              [70, 39, 6, 5, 55, 27, 38, 48, 28, 22, 34, 35, 62, 62, 15, 14, 94, 89, 86]
#            [66, 56, 68, 84, 96, 21, 34, 34, 34, 81, 62, 40, 65, 54, 62, 5, 98, 3, 2, 60]
# ....
# 7273
#                                                [7273]
#                                             [7214, 7170]
#                                          [7141, 7129, 7078]
#                                       [7028, 7089, 7042, 7069]
#                                    [6961, 7002, 7036, 7035, 6998]
#                                 [6812, 6951, 6922, 6949, 6917, 6915]
#                              [6740, 6751, 6856, 6838, 6892, 6841, 6847]
#                           [6650, 6647, 6670, 6776, 6800, 6737, 6774, 6743]
#                        [6620, 6550, 6619, 6611, 6700, 6719, 6638, 6699, 6671]
#                     [6533, 6536, 6513, 6524, 6511, 6638, 6621, 6621, 6613, 6564]
#                  [6512, 6490, 6442, 6401, 6466, 6509, 6559, 6510, 6582, 6543, 6555]
#               [6436, 6456, 6407, 6348, 6344, 6388, 6478, 6459, 6492, 6408, 6450, 6540]
#            [6358, 6325, 6403, 6327, 6247, 6260, 6295, 6446, 6378, 6395, 6397, 6413, 6489]
#         [6196, 6313, 6322, 6248, 6213, 6242, 6166, 6217, 6360, 6365, 6334, 6245, 6314, 6394]
#      [6146, 6157, 6226, 6220, 6210, 6204, 6124, 6122, 6200, 6278, 6276, 6238, 6219, 6292, 6337]
#   [6131, 6140, 6133, 6175, 6203, 6026, 6111, 6115, 6105, 6125, 6181, 6160, 6106, 6132, 6284, 6242]
# [6064, 6041, 6074, 6037, 6115, 5909, 5927, 6017, 6050, 6048, 6028, 6126, 6059, 6079, 6077, 6206, 6214]
# [5988, 5956, 6001, 6033, 6028, 5893, 5885, 5918, 5975, 5949, 5979, 6005, 6029, 5998, 6019, 6067, 6127, 6046]
# [5976, 5935, 5946, 5957, 6007, 5857, 5853, 5834, 5819, 5877, 5889, 5966, 5993, 5982, 5894, 5956, 6036, 5967, 6011]
# [5906, 5896, 5868, 5940, 5952, 5830, 5815, 5786, 5761, 5791, 5855, 5833, 5931, 5920, 5879, 5819, 5942, 5878, 5877, 5925]
# ....
# Runtime of the program is 0.0040354000
