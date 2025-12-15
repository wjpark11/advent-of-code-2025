from collections import defaultdict

with open("day07_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [line.strip() for line in inputs]


# part 1
def part1():
    splitted = 0
    beam_positions = {inputs[0].index("S")}
    for fold in inputs[1:]:
        new_beam_positions = set()
        splitted_positions = set()
        for position in beam_positions:
            if fold[position] == "^":
                splitted += 1
                splitted_positions |= {position}
                new_beam_positions |= {position - 1, position + 1}
        beam_positions |= new_beam_positions
        beam_positions -= splitted_positions
    return splitted


# part 2
def part2():
    timelines = {inputs[0].index("S"): 1}
    for fold in inputs[1:]:
        splitters_in_current_fold = [
            index for index, char in enumerate(fold) if char == "^"
        ]
        new_timelines = defaultdict(int)
        for timeline in timelines.keys():
            if timeline in splitters_in_current_fold:
                new_timelines[timeline - 1] += timelines[timeline]
                new_timelines[timeline + 1] += timelines[timeline]
            else:
                new_timelines[timeline] += timelines[timeline]
        timelines = new_timelines
    return sum(timelines.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
