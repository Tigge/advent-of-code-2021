import itertools
import math
import copy
import pprint
import collections


def generate_rotations():
    rots = [0, math.pi / 2, math.pi, 3 * math.pi / 2]
    for x in rots:
        for y in rots:
            for z in rots:
                yield [
                    [
                        round(math.cos(z) * math.cos(y)),
                        round(
                            math.cos(z) * math.sin(y) * math.sin(x)
                            - math.sin(z) * math.cos(x)
                        ),
                        round(
                            math.cos(z) * math.sin(y) * math.cos(x)
                            + math.sin(z) * math.sin(x)
                        ),
                    ],
                    [
                        round(math.sin(z) * math.cos(y)),
                        round(
                            math.sin(z) * math.sin(y) * math.sin(x)
                            + math.cos(z) * math.cos(x)
                        ),
                        round(
                            math.sin(z) * math.sin(y) * math.cos(x)
                            - math.cos(z) * math.sin(x)
                        ),
                    ],
                    [
                        round(-math.sin(y)),
                        round(math.cos(y) * math.sin(x)),
                        round(math.cos(y) * math.cos(x)),
                    ],
                ]


def mul(matrix, vector):
    return (
        vector[0] * matrix[0][0] + vector[1] * matrix[0][1] + vector[2] * matrix[0][2],
        vector[0] * matrix[1][0] + vector[1] * matrix[1][1] + vector[2] * matrix[1][2],
        vector[0] * matrix[2][0] + vector[1] * matrix[2][1] + vector[2] * matrix[2][2],
    )


def fit(base_coords, coords):

    for base in base_coords:
        for coord in coords:
            offset = base[0] - coord[0], base[1] - coord[1], base[2] - coord[2]
            offseted = {
                (coord[0] + offset[0], coord[1] + offset[1], coord[2] + offset[2])
                for coord in coords
            }
            x = base_coords & offseted

            if len(x) >= 12:
                return offset, offseted
    return None


def calculate(data):
    rotations = list(generate_rotations())

    result = data[0][1].copy()
    scanners = [(0, 0, 0)]

    beacons_left = collections.deque(data[1:])

    while len(beacons_left) > 0:
        name, coords = beacons_left.popleft()

        for rot in rotations:
            rotated_coords = {mul(rot, coord) for coord in coords}
            f = fit(result, rotated_coords)

            if f is not None:
                result |= f[1]
                scanners.append(f[0])
                break
        else:
            beacons_left.append((name, coords))

    return scanners, result


def part1(data):
    return len(data[1])


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def part2(data):
    max_distance = 0
    for a, b in itertools.combinations(data[0], 2):
        max_distance = max(max_distance, distance(a, b))

    return max_distance


def parse(f):
    def parse_item(item):
        lines = [line.strip() for line in item.splitlines()]
        return (
            lines[0],
            {
                tuple(int(axis) for axis in coordinate.split(","))
                for coordinate in lines[1:]
            },
        )

    return [parse_item(item) for item in f.read().split("\n\n")]


with open("day19.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    c = calculate(d)

    print("Part 1:", part1(c))
    print("Part 2:", part2(c))
