with open("day05_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [line.strip() for line in inputs]

fresh_ranges = [list(map(int, r.split("-"))) for r in inputs if "-" in r]
id_list = [int(i) for i in inputs if i.isdigit()]


# part 1
def part1():
    fresh_ingredients = 0
    for id in id_list:
        for r in fresh_ranges:
            if r[0] <= id <= r[1]:
                fresh_ingredients += 1
                break
    return fresh_ingredients


# part 2
def part2():
    sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])
    unoverlapped_ranges = []
    for i, r in enumerate(sorted_ranges):
        if i == 0:
            unoverlapped_ranges.append(r)
        else:
            last_range = unoverlapped_ranges[-1]
            if r[0] <= last_range[1]:
                last_range[1] = max(last_range[1], r[1])
            else:
                unoverlapped_ranges.append(r)
    total_fresh_ids = 0
    for r in unoverlapped_ranges:
        total_fresh_ids += r[1] - r[0] + 1
    return total_fresh_ids


if __name__ == "__main__":
    print(part1())
    print(part2())
