with open("day03_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [line.strip() for line in inputs]


# part1
def get_max_joltage_by_turning_two(bank: str) -> int:
    max_joltage = 0
    for i, digit1 in enumerate(bank):
        for digit2 in bank[i + 1 :]:
            joltage = int(digit1 + digit2)
            max_joltage = max(max_joltage, joltage)
    return max_joltage


def part1() -> int:
    total_joltage = 0
    for bank in inputs:
        total_joltage += get_max_joltage_by_turning_two(bank)
    return total_joltage


# part2
def get_max_joltage_by_turning_twelve(bank: str) -> int:
    max_joltage = ""
    bank_list = list(map(int, bank))
    for i in range(12, 1, -1):
        candidate_bank = bank_list[: -i + 1]
        max_value = max(candidate_bank)
        max_value_index = candidate_bank.index(max_value)
        bank_list = bank_list[max_value_index + 1 :]
        max_joltage += str(max_value)

    max_joltage += str(max(bank_list))

    return int(max_joltage)


def part2() -> int:
    total_joltage = 0
    for bank in inputs:
        total_joltage += get_max_joltage_by_turning_twelve(bank)
    return total_joltage


if __name__ == "__main__":
    print(part1())
    print(part2())
