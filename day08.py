from math import sqrt

with open("day08_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [line.strip() for line in inputs]

junction_boxes = [list(map(int, line.split(","))) for line in inputs]


def distance(box1, box2):
    return sqrt(
        (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2
    )


def get_distance_matrix(boxes):
    n = len(boxes)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i > j:
                dist_matrix[i][j] = distance(boxes[i], boxes[j])
            elif i < j:
                dist_matrix[i][j] = dist_matrix[j][i]
            else:
                dist_matrix[i][j] = 0
    return dist_matrix


print(get_distance_matrix(junction_boxes))
