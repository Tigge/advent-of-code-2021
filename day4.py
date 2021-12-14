from io import TextIOWrapper
import itertools


def score(board, numbers):
    return sum(
        map(lambda line: sum(map(lambda n: n if n not in numbers else 0, line)), board)
    )


def is_win(board, numbers):
    for line in itertools.chain(board, reversed(list(zip(*board)))):
        if all(map(lambda n: n in numbers, line)):
            return True
    return False


def parse(f: TextIOWrapper):
    numbers = list(map(int, f.readline().split(",")))
    f.readline()

    boards = []
    board = []
    for line in f.readlines():
        row = list(map(int, line.split()))
        if len(row) == 0:
            boards.append(board)
            board = []
        else:
            board.append(row)

    return (numbers, boards)


def part1(data):

    numbers, boards = data

    for i in range(1, len(numbers)):

        for board in boards:
            if is_win(board, numbers[:i]):
                return score(board, numbers[:i]) * numbers[:i][-1]
        else:
            continue
        break


def part2(data):
    numbers, boards = data

    last_looser = None
    for i in range(1, len(numbers)):
        for board in boards:
            if not is_win(board, numbers[:i]):
                last_looser = board
                break
        else:
            if last_looser is not None:
                return score(last_looser, numbers[:i]) * numbers[:i][-1]


with open("day4.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
