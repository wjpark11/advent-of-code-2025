with open("day02_input.txt", "rt") as f:
    inputs = f.readline()
    inputs = inputs.split(",")
    ranges = [list(map(int, r.split("-"))) for r in inputs]


# part1
def get_range_invalid_ids(start: int, end: int) -> range:
    start_str = str(start)
    end_str = str(end)

    if len(start_str) % 2 == 1:
        first_invalid_half = 10 ** (len(start_str) // 2)
    else:
        first_half = int(start_str[: len(start_str) // 2])
        last_half = int(start_str[len(start_str) // 2 :])
        if last_half <= first_half:
            first_invalid_half = first_half
        else:
            first_invalid_half = first_half + 1

    if len(end_str) % 2 == 1:
        last_invalid_half = 10 ** (len(end_str) // 2) - 1
    else:
        first_half = int(end_str[: len(end_str) // 2])
        last_half = int(end_str[len(end_str) // 2 :])
        if last_half >= first_half:
            last_invalid_half = first_half
        else:
            last_invalid_half = first_half - 1

    return range(first_invalid_half, last_invalid_half + 1)


def part1() -> int:
    total_invalid = 0
    for r in ranges:
        for invalid_id_half in get_range_invalid_ids(r[0], r[1]):
            total_invalid += int(str(invalid_id_half) * 2)

    return total_invalid


# part2
def is_invalid_id(product_id: int) -> bool:
    id_str = str(product_id)
    id_length = len(id_str)
    for digit in range(1, id_length // 2 + 1):
        if id_length % digit == 0:
            first_chunk = id_str[:digit]
            if first_chunk * (id_length // digit) == id_str:
                return True
    return False


def part2() -> int:
    total_invalid_id_sum = 0
    for r in ranges:
        for product_id in range(r[0], r[1] + 1):
            if is_invalid_id(product_id):
                total_invalid_id_sum += product_id
    return total_invalid_id_sum


if __name__ == "__main__":
    print(part1())
    print(part2())
