from io import TextIOWrapper
import itertools
import functools
import copy
import math


MAP = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

SCORE1 = {
    None: 0,
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

SCORE2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def validate(line):

    stack = []

    for n, c in enumerate(line):
        if c in MAP.values():
            stack.append(c)
        else:
            if MAP[c] != stack.pop():
                return (c, stack)

    return (None, stack)


def part1(lines):
    scores = list(map(lambda line: SCORE1[validate(line)[0]], lines))
    return sum(scores)


def part2(lines):
    def score(stack):
        s = 0
        for token in reversed(stack):
            s = s * 5 + SCORE2[token]
        return s

    things = filter(lambda p: p[0] is None, map(lambda line: validate(line), lines))
    scores = sorted(map(lambda t: score(t[1]), things))

    return scores[len(scores) // 2]


def parse(f):
    return list(map(lambda line: line.strip(), f.readlines()))


with open("day10.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
