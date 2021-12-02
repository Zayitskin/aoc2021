

def part1(data: object) -> None:

    x: int = 0
    depth: int = 0

    for line in data:
        cmd, val = line.split(" ")
        if cmd == "forward":
            x += int(val)
        elif cmd == "up":
            depth -= int(val)
        elif cmd == "down":
            depth += int(val)
            

    print(f"Part 1: {x * depth}")

def part2(data: object) -> None:

    depth: int = 0
    aim: int = 0
    x: int = 0

    for line in data:
        cmd, val = line.split(" ")
        if cmd == "forward":
            x += int(val)
            depth += aim * int(val)
        elif cmd == "up":
            aim -= int(val)
        elif cmd == "down":
            aim += int(val)

    print(f"Part 2: {x * depth}")


if __name__ == "__main__":

    with open("data.txt") as data:
        part1(data)
        pass
    with open("data.txt") as data:
        part2(data)
        pass
