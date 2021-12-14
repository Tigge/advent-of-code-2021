import itertools
import operator


def bits2int(bits):
    return int("".join(map(str, bits)), 2)


def part1(bits_list):

    bit_count = [0] * len(bits_list[0])
    for bits in bits_list:
        for n, bit in enumerate(bits):
            bit_count[n] += bit

    half = len(bits_list) / 2

    gamma = bits2int(map(lambda v: 1 if v > half else 0, bit_count))
    epsilon = bits2int(map(lambda v: 1 if v <= half else 0, bit_count))

    return gamma * epsilon


def filter_list(bits_list, index, op):

    bit_count = sum([bits[index] for bits in bits_list])
    half = len(bits_list) / 2

    return list(
        filter(lambda bs: bs[index] == (1 if op(bit_count, half) else 0), bits_list)
    )


def part2(bits_list):

    oxygen_generator_list = bits_list[:]
    for n in range(len(oxygen_generator_list[0])):
        oxygen_generator_list = filter_list(oxygen_generator_list, n, operator.lt)
        if len(oxygen_generator_list) == 1:
            break
    oxygen_generator_rating = bits2int(oxygen_generator_list[0])

    co2_scrubber_list = bits_list[:]
    for n in range(len(co2_scrubber_list[0])):
        co2_scrubber_list = filter_list(co2_scrubber_list, n, operator.ge)
        if len(co2_scrubber_list) == 1:
            break
    co2_scrubber_rating = bits2int(co2_scrubber_list[0])

    return oxygen_generator_rating * co2_scrubber_rating


def parse(f):
    return map(lambda line: list(map(int, line.strip())), f.readlines())


with open("day3.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
