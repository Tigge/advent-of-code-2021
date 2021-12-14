from io import TextIOWrapper
import itertools
import functools
import copy
import math


def debug(state):
    for y, line in enumerate(state):
        for x, level in enumerate(line):
            print(level, end="")
        print("")
    print()


def flash(state, p):
    x, y = p

    if state[y][x] < 10 or state[y][x] >= 100:
        return

    state[y][x] = 100
    yield p

    for dy in range(-1, 2):
        if y + dy < 0 or y + dy >= len(state):
            continue
        for dx in range(-1, 2):
            if x + dx < 0 or x + dx >= len(state):
                continue

            if dx == 0 and dy == 0:
                continue

            state[y + dy][x + dx] += 1
            yield from flash(state, (x + dx, y + dy))


def process_flash(state):
    for y, line in enumerate(state):
        for x, level in enumerate(line):
            if level > 9:
                yield from flash(state, (x, y))

    yield from ()


def process(state):
    for y, line in enumerate(state):
        for x, level in enumerate(line):
            state[y][x] += 1

    flashes = list(process_flash(state))

    for x, y in flashes:
        state[y][x] = 0

    return len(flashes)


def part1(state):
    flashes = 0
    for n in range(100):
        flashes += process(state)
    return flashes


def part2(state):
    for n in itertools.count(1):
        if process(state) == 100:
            return n


def parse(f):
    return list(map(lambda line: list(map(int, line.strip())), f.readlines()))


with open("day11.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(copy.deepcopy(d)))
    print("Part 2:", part2(copy.deepcopy(d)))
