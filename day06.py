import re

with open("day06_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [line for line in inputs]

sheet = [re.findall(r"\d+|[\*\+]", line) for line in inputs]


# part 1
def solver(sheet_column: list) -> int:
    numbers, operator = sheet_column[:-1], sheet_column[-1]
    if operator == "+":
        return sum(int(num) for num in numbers)
    elif operator == "*":
        result = 1
        for num in numbers:
            result *= int(num)
        return result


def part1():
    grand_total = 0
    for i, _ in enumerate(sheet[0]):
        grand_total += solver([line[i] for line in sheet])

    return grand_total


# part 2
operator_row = inputs[-1]
start_positions = [i for i, char in enumerate(operator_row) if char in "*+"]
operators = [operator_row[i] for i in start_positions]
problems = [
    [row[start_positions[i] : start_positions[i + 1] - 1] for row in inputs[:-1]]
    + [operators[i]]
    for i, _ in enumerate(start_positions)
    if i + 1 < len(start_positions)
] + [
    [row[start_positions[-1] :].replace("\n", "") for row in inputs[:-1]]
    + [operators[-1]]
]


def solver2(sheet_column: list) -> int:
    numbers, operator = sheet_column[:-1], sheet_column[-1]
    transposed_numbers = []
    for zipped in zip(*numbers):
        transposed_numbers.append(int("".join(zipped)))
    if operator == "+":
        return sum(transposed_numbers)
    elif operator == "*":
        result = 1
        for num in transposed_numbers:
            result *= num
        return result


def part2():
    grand_total = 0
    for problem in problems:
        grand_total += solver2(problem)
    return grand_total


if __name__ == "__main__":
    print(part1())
    print(part2())
