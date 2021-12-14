import itertools


def find_position(commands):
    x, y = 0, 0
    for (direction, n) in commands:
        if direction == "forward":
            x += n
        elif direction == "down":
            y += n
        elif direction == "up":
            y -= n
    return x * y


def find_position2(commands):
    x, y, aim = 0, 0, 0

    for (direction, n) in commands:
        if direction == "forward":
            x += n
            y += aim * n
        elif direction == "down":
            aim += n
        elif direction == "up":
            aim -= n

    return x * y


def parse(f):
    return map(lambda p: (p[0], int(p[1])), map(lambda l: l.split(" "), f.readlines()))


with open("day2.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))
    print("Part 1:", find_position(d))
    print("Part 2:", find_position2(d))
