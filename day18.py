import itertools
import math
import copy


def explode(number):
    p, depth = 0, 0
    next_number = []
    next_number_add = 0
    exploded = False
    while p < len(number):
        token = number[p]
        if token == "[":
            depth += 1
            if depth > 4 and not exploded:
                prev_number_add = number[p + 1]
                next_number_add = number[p + 3]
                for i in range(len(next_number) - 1, 0, -1):
                    if type(next_number[i]) is int:
                        next_number[i] += prev_number_add
                        break
                token = 0
                p += 4
                exploded = True
        elif token == "]":
            depth -= 1
        elif type(token) is int:
            token += next_number_add
            next_number_add = 0

        next_number.append(token)
        p += 1

    return next_number


def split(number):
    p = 0
    next_number = []
    splitted = False
    while p < len(number):
        token = number[p]
        if type(token) is int and token >= 10 and not splitted:
            next_number += ["[", math.floor(token / 2), ",", math.ceil(token / 2), "]"]
            splitted = True
        else:
            next_number.append(token)
        p += 1
    return next_number


def reduce(number):
    prev = []
    while prev != number:
        prev = copy.deepcopy(number)
        number = explode(number)
        if number != prev:
            continue
        number = split(number)
    return number


def add(a, b):
    return reduce(["["] + a + [","] + b + ["]"])


def magnitude(number):

    while len(number) > 1:
        p = 0
        next_number = []
        while p < len(number):
            if (
                number[p] == "["
                and type(number[p + 1]) is int
                and number[p + 2] == ","
                and type(number[p + 3]) is int
                and number[p + 4] == "]"
            ):
                next_number.append(3 * number[p + 1] + 2 * number[p + 3])
                p += 4
            else:
                next_number.append(number[p])

            p += 1
        number = next_number
    return number[0]


def part1(data):
    res = data[0]
    for number in data[1:]:
        res = add(res, number)

    return magnitude(res)


def part2(data):

    largest = 0
    for a, b in itertools.permutations(data, 2):
        largest = max(largest, magnitude(add(a, b)))

    return largest


def parse(f):
    return [
        [int(token) if token.isdecimal() else token for token in list(line.strip())]
        for line in f.readlines()
    ]


with open("day18.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
