from io import TextIOWrapper
import itertools
import functools

PATTERNS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdef": 8,
    "abcdfg": 9,
}


def deduce(patterns):
    known = {}

    for pattern in sorted(patterns, key=len):
        p = set(pattern)

        if len(p) == 2:
            known[1] = p
        elif len(p) == 3:
            known[7] = p
        elif len(p) == 4:
            known[4] = p
        elif len(p) == 5:
            # 2, 3, 5
            if known[1] < p:
                known[3] = p
            elif (known[4] - known[1]) < p:
                known[5] = p
            else:
                known[2] = p
        elif len(p) == 6:
            # 0, 6, 9
            if not (known[1] < p):
                known[6] = p
            elif known[5] < p:
                known[9] = p
            else:
                known[0] = p
        elif len(p) == 7:
            known[8] = p

    return dict(map(lambda i: ("".join(sorted(i[1])), i[0]), known.items()))


def part1(segments):
    outputs = map(lambda s: s[1], segments)
    values = list(itertools.chain(*outputs))

    return len(
        list(
            filter(
                lambda v: len(v) == 2 or len(v) == 4 or len(v) == 3 or len(v) == 7,
                values,
            )
        )
    )


def part2(positions):
    total = 0
    for a, b in positions:
        m = deduce(a)
        v = "".join(list(map(lambda v: str(m["".join(sorted(v))]), b)))
        total += int(v)
    return total


def parse(f):
    return list(
        map(
            lambda line: list(map(lambda t: t.split(), line.strip().split(" | "))),
            f.readlines(),
        )
    )


with open("day8.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
