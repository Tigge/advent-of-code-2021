import collections


def calculate(template, rules, steps):
    cache = {}

    def calculate_pair(pair, steps):
        if steps == 0:
            return collections.Counter()
        if (pair, steps) in cache:
            return cache[(pair, steps)]

        letter = rules[pair]
        counter = (
            collections.Counter(letter)
            + calculate_pair(pair[0] + letter, steps - 1)
            + calculate_pair(letter + pair[1], steps - 1)
        )

        cache[(pair, steps)] = counter

        return counter

    counter = collections.Counter(template)
    for i in range(len(template) - 1):
        counter += calculate_pair(template[i : i + 2], steps)
    return counter


def score(calculation):
    things = calculation.most_common()
    return things[0][1] - things[-1][1]


def part1(data):
    return score(calculate(data[0], data[1], 10))


def part2(data):
    return score(calculate(data[0], data[1], 40))


def parse(f):
    return (
        f.readline().strip(),
        {item[0:2]: item[6] for item in f.read().strip().split("\n")},
    )


with open("day14.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
