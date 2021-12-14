from io import TextIOWrapper
import functools


def find_paths(graph, extra=False):
    def visit(graph, node, visited, extra_visit):
        next_visited = visited + [node]
        next_extra_visit = extra_visit or (
            node.islower() and next_visited.count(node) >= 2
        )
        if node == "end":
            yield next_visited
            return

        for next_node in graph[node]:
            if next_node.islower() and (next_extra_visit and next_node in next_visited):
                continue
            yield from visit(graph, next_node, next_visited, next_extra_visit)

    yield from visit(graph, "start", [], extra)


def part1(graph):
    return len(list(find_paths(graph, extra=True)))


def part2(graph):
    return len(list(find_paths(graph, extra=False)))


def parse(f):
    def parse_pairs(m, p):
        n1, n2 = p
        if n1 != "end" and n2 != "start":
            m.setdefault(n1, []).append(n2)
        if n1 != "start" and n2 != "end":
            m.setdefault(n2, []).append(n1)
        return m

    return functools.reduce(
        parse_pairs, [line.strip().split("-") for line in f.readlines()], {}
    )


with open("day12.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
