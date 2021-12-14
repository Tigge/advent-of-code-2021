from io import TextIOWrapper
from typing import Set


def debug(positions: Set):
    for y in range(max([p[1] for p in positions]) + 1):
        for x in range(max([p[0] for p in positions]) + 1):
            print("#" if (x, y) in positions else ".", end="")
        print()
    print()


def fold(positions, fold):
    next_positions = set()

    for position in positions:
        if fold[0] == "x" and position[0] > fold[1]:
            next_positions.add((fold[1] - (position[0] - fold[1]), position[1]))
        elif fold[0] == "y" and position[1] > fold[1]:
            next_positions.add((position[0], fold[1] - (position[1] - fold[1])))
        else:
            next_positions.add((position[0], position[1]))

    return next_positions


def part1(data):
    positions, folds = data
    positions = fold(positions, folds[0])

    return len(positions)


def part2(data):
    positions, folds = data

    for f in folds:
        positions = fold(positions, f)
    debug(positions)


def parse(f):
    postitions, folds = f.read().strip().split("\n\n")

    return (
        set(
            tuple(int(num) for num in line.split(","))
            for line in postitions.split("\n")
        ),
        [(line[11:12], int(line[13:])) for line in folds.split("\n")],
    )


with open("day13.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
