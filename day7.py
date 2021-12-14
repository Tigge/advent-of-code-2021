def part1(positions):
    ymin = min(positions)
    ymax = max(positions)

    fuels = []
    for n in range(ymin, ymax):
        fuel = sum(map(lambda m: abs(m - n), positions))
        fuels.append(fuel)

    return min(fuels)


def triangular_number(n):
    return (n * (n + 1)) // 2


def part2(positions):
    ymin = min(positions)
    ymax = max(positions)

    fuels = []
    for n in range(ymin, ymax):
        fuel = sum(map(lambda m: triangular_number(abs(m - n)), positions))
        fuels.append(fuel)

    return min(fuels)


def parse(f):
    return list(map(int, f.readline().strip().split(",")))


with open("day7.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
