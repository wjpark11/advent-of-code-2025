from itertools import combinations

with open("day10_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [line.strip() for line in inputs]

manuals = []
for line in inputs:
    manual = {"indicator": {}, "buttons": [], "joltages": []}
    line_parts = line.split(" ")
    indicator_line = line_parts[0].strip("[]")
    manual["indicator"] = {
        index for index, char in enumerate(indicator_line) if char == "#"
    }
    buttons_line = line_parts[1:-1]
    for button in buttons_line:
        manual["buttons"].append({int(x) for x in button.strip("()").split(",")})
    joltages_line = line_parts[-1].strip("{}")
    manual["joltages"] = [int(x) for x in joltages_line.split(",")]
    manuals.append(manual)


# part 1
def get_minimal_button_presses(indicator: set[int], buttons: list[set[int]]) -> int:
    button_presses = 1
    while True:
        for combi in combinations(buttons, r=button_presses):
            pressed_indicators = set()
            for button in combi:
                pressed_indicators ^= button
            if pressed_indicators == indicator:
                return button_presses
        button_presses += 1


def part1():
    total_button_presses = 0
    for manual in manuals:
        total_button_presses += get_minimal_button_presses(
            manual["indicator"], manual["buttons"]
        )
    return total_button_presses


# part 2
def interger_partitions(n: int, k: int) -> list[int]:
    if k == 1:
        return [[n]]
    partitions = []
    for i in range(0, n - k + 1):
        for p in interger_partitions(n - i, k - 1):
            partitions.append([i] + p)
    return partitions


if __name__ == "__main__":
    print(part1())
    print(interger_partitions(7, 4))
