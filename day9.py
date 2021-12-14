from io import TextIOWrapper
import itertools
import functools
import copy
import math


def get(segments, x, y):

    if y < 0 or y >= len(segments):
        return 10
    if x < 0 or x >= len(segments[y]):
        return 10
    return segments[y][x]


def find_low_points(segments):
    points = []

    for y, line in enumerate(segments):
        for x, v in enumerate(line):

            up = get(segments, x, y - 1)
            right = get(segments, x + 1, y)
            down = get(segments, x, y + 1)
            left = get(segments, x - 1, y)

            if v < up and v < right and v < down and v < left:
                points.append((x, y))
    return points


def part1(segments):
    points = find_low_points(segments)
    return sum(map(lambda p: segments[p[1]][p[0]], points)) + len(points)


def flood_fill(segments, point):

    x, y = point

    if y < 0 or y >= len(segments):
        return 0
    if x < 0 or x >= len(segments[y]):
        return 0
    if segments[y][x] != " ":
        return 0

    segments[y][x] = "."

    return (
        1
        + flood_fill(segments, (x, y + 1))
        + flood_fill(segments, (x, y - 1))
        + flood_fill(segments, (x + 1, y))
        + flood_fill(segments, (x - 1, y))
    )


def part2(segments):

    points = []

    for y, line in enumerate(segments):
        for x, v in enumerate(line):
            if v == 9:
                points.append((x, y))

    f = copy.deepcopy(segments)
    for y, line in enumerate(f):
        for x, v in enumerate(line):
            f[y][x] = " "

    for (x, y) in points:
        f[y][x] = "X"

    areas = []
    for y, line in enumerate(f):
        for x, v in enumerate(line):
            if f[y][x] != " ":
                continue
            areas.append(flood_fill(f, (x, y)))

    return math.prod(sorted(areas)[-3:])


def parse(f):
    return list(map(lambda l: list(map(int, list(l.strip()))), f.readlines()))


with open("day9.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
