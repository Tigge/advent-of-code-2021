from io import TextIOWrapper


def sign(n):
    return 0 if n == 0 else 1 if n > 0 else -1


def intersections(lines):
    points = {}
    for p1, p2 in lines:
        xd = sign(p2[0] - p1[0])
        yd = sign(p2[1] - p1[1])
        l = max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1])) + 1
        for n in range(l):
            coord = (p1[0] + xd * n, p1[1] + yd * n)
            points[coord] = points.get(coord, 0) + 1

    return len(list(filter(lambda n: n > 1, points.values())))


def parse(f: TextIOWrapper):
    parts = map(lambda l: l.strip().split(" -> "), f.readlines())
    parts = map(
        lambda p: (list(map(int, p[0].split(","))), list(map(int, p[1].split(",")))),
        parts,
    )
    return list(parts)


def part1(lines):
    lines = [l for l in lines if l[0][0] == l[1][0] or l[0][1] == l[1][1]]
    return intersections(lines)


def part2(lines):
    return intersections(lines)


with open("day5.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
