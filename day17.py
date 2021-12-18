import itertools
import math


def triangular_number(n):
    return (n * (n + 1)) // 2


def find_x(target):
    for vx in range(target[1] + 1):
        vxc = vx
        x = 0
        for n in itertools.count():
            x += vxc
            if x > target[1]:
                break
            elif x >= target[0]:
                yield ([n, math.inf if vxc == 0 else n], vx)

            if vxc == 0:
                break
            vxc = max(0, vxc - 1)


def find_y(target):

    for vy in range(abs(target[0]), target[0] - 1, -1):
        vyc = vy
        y = 0
        for n in itertools.count():
            y += vyc

            if y < target[0]:
                break
            elif y <= target[1]:
                yield (n, vy)
            vyc -= 1


def part1(data):
    possible_y = list(find_y(data["y"]))
    return max([triangular_number(item[1]) for item in possible_y])


def part2(data):
    possible_x = list(find_x(data["x"]))
    possible_y = list(find_y(data["y"]))

    possible = set()
    for yn, vy in possible_y:
        for xn, vx in possible_x:
            if yn >= xn[0] and yn <= xn[1]:
                possible.add((vx, vy))

    return len(possible)


def parse(f):
    def parse_item(thing):
        axis, r = thing.split("=")
        return (axis, tuple(int(num) for num in r.split("..")))

    return {
        item[0]: item[1]
        for item in [parse_item(item) for item in f.read().strip()[13:].split(", ")]
    }


with open("day17.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
