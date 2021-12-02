

def part1(data: object) -> None:

    depth: int = 0
    inc: int = -1
    for line in data:
        if int(line) > depth:
            inc += 1
        depth = int(line)

    print(f"Part 1: {inc}")

def part2(data: str) -> None:

    depths: list[int] = [int(line) for line in data]
    inc: int = -1
    prev: int = 0
    for i in range(0, len(depths) - 2):
        if depths[i] + depths[i + 1] + depths[i + 2] > prev:
            inc += 1
        prev = depths[i] + depths[i + 1] + depths[i + 2]

    print(f"Part 2: {inc}")


if __name__ == "__main__":

    with open("data.txt") as data:
        part1(data)
        pass
    with open("data.txt") as data:
        part2(data)
        pass
