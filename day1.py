import itertools


def find_increases(numbers):
    return len(list(filter(lambda n: n[0] < n[1], zip(numbers[:-1], numbers[1:]))))


def find_triplet_increases(numbers):
    return find_increases(list(map(sum, zip(numbers[:], numbers[1:], numbers[2:]))))


def parse(f):
    return map(lambda l: int(l), f.readlines())


with open("day1.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))
    print("Part 1:", find_increases(d))
    print("Part 2:", find_triplet_increases(d))
