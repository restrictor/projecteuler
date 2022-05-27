""" Path sum: four ways

    Problem 83
    NOTE: This problem is a significantly more challenging version of Problem 81.

    In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right,
    up, and down, is indicated in bold red and is equal to 2297.

        131 673 234 103  18
        201  96 342 965 150
        630 803 746 422 111
        537 699 497 121 956
        805 732 524  37 331

        (red path -> 131 201 96 342 103 18 150 111 422 121 37 331)

    Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in
    matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

from time import perf_counter
start = perf_counter()

import sys
from csv import reader
from numpy import array, zeros
from copy import deepcopy


# I used an existing implementation of dijkstra algoritm.
# https://www.educative.io/edpresso/how-to-implement-dijkstras-algorithm-in-python


def read_graph() -> (array, array, dict):
    with open("../data/083.txt", 'r') as temp:
        mat = array([list(map(int, x)) for x in reader(temp, delimiter=',')])

    edges = zeros((len(mat) * len(mat), len(mat) * len(mat)))
    origin = {}

    # create all edges
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i > 0:
                edges[i + j * len(mat), i - 1 + j * len(mat)] = mat[i - 1, j]
            if j > 0:
                edges[i + j * len(mat), i + (j - 1) * len(mat)] = mat[i, j - 1]
            if i < len(mat) - 1:
                edges[i + j * len(mat), i + 1 + j * len(mat)] = mat[i + 1, j]
            if j < len(mat) - 1:
                edges[i + j * len(mat), i + (j + 1) * len(mat)] = mat[i, j + 1]
            origin[i + j * len(mat)] = mat[i, j]

    vertices = deepcopy(edges)
    vertices[vertices != 0] = 1
    return vertices, edges, origin


# Function to find out which of the unvisited node needs to be visited next
def to_be_visited(number_of_vertices: int, visited_and_distance: list[list]) -> int:
    v = -10

    # Choosing the vertex with the minimum distance
    for index in range(number_of_vertices):
        if visited_and_distance[index][0] == 0 and \
                (v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1]):
            v = index
    return v


def dijkstra(vertices: array, edges: array, origin: dict) -> None:
    number_of_vertices = len(vertices[0])

    # The first element of the lists inside visited_and_distance denotes if the vertex has been visited.
    # The second element of the lists inside the visited_and_distance denotes the distance from the source.
    visited_and_distance = [[0, 0]]
    for i in range(number_of_vertices - 1):
        visited_and_distance.append([0, sys.maxsize])

    for vertex in range(number_of_vertices):

        # Finding the next vertex to be visited.
        to_visit = to_be_visited(number_of_vertices, visited_and_distance)

        for neighbor_index in range(number_of_vertices):

            # Calculating the new distance for all unvisited neighbours of the chosen vertex.
            if vertices[to_visit][neighbor_index] == 1 and visited_and_distance[neighbor_index][0] == 0:
                new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbor_index]

                # Updating the distance of the neighbor if its current distance
                # is greater than the distance that has just been calculated
                if visited_and_distance[neighbor_index][1] > new_distance:
                    visited_and_distance[neighbor_index][1] = new_distance

            # Visiting the vertex found earlier
            visited_and_distance[to_visit][0] = 1

    bottom_right = [visited_and_distance[-1]]
    print(f"The shortest distance from top-left to bottom-right is: {visited_and_distance[-1][1] + origin[0]}")


def main():

    vertices, edges, origin = read_graph()
    dijkstra(vertices, edges, origin)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# The shortest distance from top-left to bottom-right is: 425185.0
# Runtime of the program is 16.8903430000

