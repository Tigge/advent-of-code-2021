import itertools
import collections

NEIGHBORS = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (0, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def get(image, x, y, default):
    if y < 0 or y >= len(image) or x < 0 or x >= len(image[y]):
        return default
    return image[y][x]


def pix2int(pixels):
    return int("".join(["0" if pixel == "." else "1" for pixel in pixels]), 2)


def enhance(image, iea, times):
    default = "."
    for n in range(times):
        next_image = []
        height, width = len(image), len(image[0])

        for y in range(-1, height + 1):
            next_line = ""
            for x in range(-1, width + 1):
                next_line += iea[
                    pix2int(
                        [get(image, x + n[0], y + n[1], default) for n in NEIGHBORS]
                    )
                ]
            next_image.append(next_line)

        image = next_image
        default = iea[pix2int([default] * 9)]

    return image


def part1(data):
    image = enhance(data[1], data[0], 2)
    return collections.Counter(itertools.chain.from_iterable(image))["#"]


def part2(data):
    image = enhance(data[1], data[0], 50)
    return collections.Counter(itertools.chain.from_iterable(image))["#"]


def parse(f):
    lines = [line.strip() for line in f.readlines()]
    return (lines[0], lines[2:])


with open("day20.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
