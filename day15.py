import collections
import math
import queue


def dijkstra(graph, source, target):

    prev = {}
    dist = {source: 0}
    q = queue.PriorityQueue()

    for y, line in enumerate(graph):
        for x, char in enumerate(line):
            if (x, y) != source:
                dist[(x, y)] = math.inf
                prev[(x, y)] = None
            q.put((dist[(x, y)], (x, y)))

    while not q.empty():
        (_, u) = q.get()

        if u == target:
            break

        for nd in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            v = (u[0] + nd[0], u[1] + nd[1])
            if v not in dist:
                continue

            alt = dist[u] + int(graph[v[1]][v[0]])
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                q.put((alt, v))

    return dist, prev


def path(target, prev, dist):
    S = []
    u = target
    while u is not None:
        S.insert(0, (u, dist[u]))
        u = prev.get(u, None)

    return S


def part1(graph):
    target = len(graph[0]) - 1, len(graph) - 1
    data = dijkstra(graph, (0, 0), target)
    return data[0][target]


def add(graph, increase):
    return [
        [
            (num + increase) if (num + increase) <= 9 else (num + increase) - 9
            for num in line
        ]
        for line in graph
    ]


def part2(graph):
    multi_graph = []
    for y in range(5):
        multi_graph += [[] for _ in range(len(graph))]
        for x in range(5):
            added_graph = add(graph, y + x)
            for n, line in enumerate(added_graph):
                multi_graph[-len(graph) + n] += line

    target = len(multi_graph[0]) - 1, len(multi_graph) - 1
    data = dijkstra(multi_graph, (0, 0), target)
    return data[0][target]


def parse(f):
    return [[int(char) for char in line.strip()] for line in f.readlines()]


with open("day15.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
