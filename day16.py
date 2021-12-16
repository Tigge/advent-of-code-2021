import math


def parse_packets(data, p, max_packets, max_bits):

    packets = []

    while len(data) - p >= 4:
        if len(packets) >= max_packets or p >= max_bits:
            break
        packet_version = int(data[p + 0 : p + 3], 2)
        packet_type_id = int(data[p + 3 : p + 6], 2)
        p += 6

        # Literal
        if packet_type_id == 4:
            result = ""
            last_group = 1
            while last_group == 1:
                last_group = int(data[p], 2)
                result += data[p + 1 : p + 5]
                p += 5

            packets.append((p, (packet_version, packet_type_id, int(result, 2))))

        # Operator
        else:
            length_type_id = int(data[p], 2)
            subpackets = []
            if length_type_id == 0:
                subpackets_length = int(data[p + 1 : p + 16], 2)
                p, subpackets = parse_packets(
                    data, p + 16, 9999, p + 16 + subpackets_length
                )

            if length_type_id == 1:
                subpackets_count = int(data[p + 1 : p + 12], 2)
                p, subpackets = parse_packets(data, p + 12, subpackets_count, 9999)

            packets.append((p, (packet_version, packet_type_id, subpackets)))

    return (p, packets)


def version_sum(packets):
    count = 0
    for _, packet in packets:
        if type(packet[2]) is list:
            count += packet[0] + version_sum(packet[2])
        else:
            count += packet[0]
    return count


def part1(data):
    packets = parse_packets(data, 0, 1, 99999)
    return version_sum(packets[1])


def evaluate(packet):
    _, p = packet

    if p[1] == 0:
        return sum(map(evaluate, p[2]))
    elif p[1] == 1:
        return math.prod(map(evaluate, p[2]))
    elif p[1] == 2:
        return min(map(evaluate, p[2]))
    elif p[1] == 3:
        return max(map(evaluate, p[2]))
    elif p[1] == 4:
        return p[2]
    elif p[1] == 5:
        t1, t2 = evaluate(p[2][0]), evaluate(p[2][1])
        return 1 if t1 > t2 else 0
    elif p[1] == 6:
        t1, t2 = evaluate(p[2][0]), evaluate(p[2][1])
        return 1 if t1 < t2 else 0
    elif p[1] == 7:
        t1, t2 = evaluate(p[2][0]), evaluate(p[2][1])
        return 1 if t1 == t2 else 0


def part2(data):
    packets = parse_packets(data, 0, 1, 99999)
    return evaluate(packets[1][0])


def parse(f):
    return "".join([format(int(char, 16), "04b") for char in f.read().strip()])
    return [[int(char) for char in line.strip()] for line in f.readlines()]


with open("day16.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
