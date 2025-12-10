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


if __name__ == "__main__":
    print(part1())
