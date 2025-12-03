with open("day01_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]


def get_position(current_positon: int, dial: str) -> int:
    direction, steps = dial[0], int(dial[1:])
    if direction == "R":
        current_positon += steps
    elif direction == "L":
        current_positon -= steps
    return current_positon % 100


# Part 1
def part1(inputs: list) -> int:
    position = 50
    position_list = []
    for dial in inputs:
        position = get_position(position, dial)
        position_list.append(position)
    return len(list(filter(lambda x: x == 0, position_list)))


# Part 2
def hit_zero_times(current_position: int, dial: str) -> int:
    direction, steps = dial[0], int(dial[1:])
    hit_zero = 0
    if direction == "R":
        steps_for_hit_zero = 100 - current_position
        if steps >= steps_for_hit_zero:
            hit_zero = 1 + ((steps - steps_for_hit_zero) // 100)
    elif direction == "L":
        if current_position == 0:
            current_position = 100
        steps_for_hit_zero = current_position
        if steps >= steps_for_hit_zero:
            hit_zero = 1 + ((steps - steps_for_hit_zero) // 100)
    return hit_zero


def part2(inputs: list) -> int:
    position = 50
    total_hit_zero = 0
    for dial in inputs:
        total_hit_zero += hit_zero_times(position, dial)
        position = get_position(position, dial)
    return total_hit_zero


if __name__ == "__main__":
    print(part1(inputs))
    print(part2(inputs))
