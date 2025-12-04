with open("day04_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [line.strip() for line in inputs]
    grid = [list(line) for line in inputs]


# part1
def count_adjacent_rolls(row: int, col: int) -> int:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == "@":
                count += 1
    return count


def part1() -> int:
    accecible_rolls = 0
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if _ == "@":
                accecible_rolls += 1 if count_adjacent_rolls(i, j) < 4 else 0
    return accecible_rolls


# part2
def get_accecible_rolls_and_next_grid(
    grid: list[list[str]],
) -> tuple[int, list[list[str]]]:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    accecible_rolls = 0
    next_grid = [row.copy() for row in grid]

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if _ == "@":
                count = 0
                for dr, dc in directions:
                    r, c = i + dr, j + dc
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        if grid[r][c] == "@":
                            count += 1
                if count < 4:
                    next_grid[i][j] = "."
                    accecible_rolls += 1
    return accecible_rolls, next_grid


def part2() -> int:
    total_accecible_rolls = 0
    current_grid = grid
    while True:
        accecible_rolls, next_grid = get_accecible_rolls_and_next_grid(current_grid)
        total_accecible_rolls += accecible_rolls
        if next_grid == current_grid:
            break
        current_grid = next_grid
    return total_accecible_rolls


if __name__ == "__main__":
    print(part1())
    print(part2())
