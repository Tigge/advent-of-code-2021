def simulate(state, days):
    def iterate(state):
        return [
            state[1],
            state[2],
            state[3],
            state[4],
            state[5],
            state[6],
            state[0] + state[7],
            state[8],
            state[0],
        ]

    for n in range(days):
        state = iterate(state)

    return sum(state)


def part1(state):
    return simulate(state, 80)


def part2(state):
    return simulate(state, 256)


def parse(f):
    state = [0] * 9
    for n in map(int, f.readline().strip().split(",")):
        state[n] += 1
    return state


with open("day6.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
