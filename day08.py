from math import sqrt

with open("day08_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [line.strip() for line in inputs]

junction_boxes = {
    idx: list(map(int, line.split(","))) for idx, line in enumerate(inputs)
}


def distance(box1, box2):
    return sqrt(
        (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2
    )


# part 1
def get_shortest_1000_pairs(boxes):
    distances = dict()
    for i in boxes.keys():
        for j in boxes.keys():
            if i < j:
                distances[(i, j)] = distance(boxes[i], boxes[j])
    shortest_pairs = dict(
        sorted(distances.items(), key=lambda item: item[1])[:1000]
    ).keys()
    return list(shortest_pairs)


def find_circuit(pairs, box_idx):
    circuit = {box_idx}
    while True:
        added = False
        for pair in pairs:
            if circuit & set(pair):
                circuit |= set(pair)
                pairs.remove(pair)
                added = True
        if not added:
            break
    return circuit


def part1():
    circuit_list = []
    connecting_pairs = get_shortest_1000_pairs(junction_boxes)
    indexes = {pair[0] for pair in connecting_pairs} | {
        pair[1] for pair in connecting_pairs
    }
    while indexes:
        box_idx = indexes.pop()
        circuit = find_circuit(connecting_pairs, box_idx)
        circuit_list.append(circuit)
        indexes -= circuit
    circuit_sizes = sorted([len(circuit) for circuit in circuit_list], reverse=True)
    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]


# part 2
def get_sorted_pairs(boxes):
    distances = dict()
    for i in boxes.keys():
        for j in boxes.keys():
            if i < j:
                distances[(i, j)] = distance(boxes[i], boxes[j])
    sorted_pairs = dict(sorted(distances.items(), key=lambda item: item[1])).keys()
    return list(sorted_pairs)


box_indexes = set(junction_boxes.keys())


def part2(all_indexes):
    sorted_pairs = get_sorted_pairs(junction_boxes)
    first_pair = sorted_pairs[0]
    lower_bound = len(junction_boxes) - 1
    upper_bound = 100000
    half_way = (lower_bound + upper_bound) // 2
    while True:
        circuit = find_circuit(sorted_pairs[:half_way], first_pair[0])
        if circuit == all_indexes:
            upper_bound = half_way
        else:
            lower_bound = half_way
        if lower_bound + 1 == upper_bound:
            break
        half_way = (lower_bound + upper_bound) // 2
        print(f"Trying with {half_way} pairs...")
    final_pair = sorted_pairs[upper_bound - 1]
    return junction_boxes[final_pair[0]][0] * junction_boxes[final_pair[1]][0]


if __name__ == "__main__":
    print(part1())
    print(part2(box_indexes.copy()))
