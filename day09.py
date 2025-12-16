with open("day09_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [line.strip() for line in inputs]

red_tiles = [list(map(int, line.split(","))) for line in inputs]


def part1():
    max_area = 0
    for i, start_tile in enumerate(red_tiles):
        for end_tile in red_tiles[i + 1 :]:
            max_area = max(
                max_area,
                (abs(start_tile[0] - end_tile[0]) + 1)
                * (abs(start_tile[1] - end_tile[1]) + 1),
            )
    return max_area


if __name__ == "__main__":
    print(part1())
