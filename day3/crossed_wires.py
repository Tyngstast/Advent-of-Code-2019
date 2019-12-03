import os


def run():
    basedir = os.path.abspath(os.path.dirname(__file__))
    in_file = os.path.join(basedir, 'crossed_wires.in')

    with open(in_file) as f:
        w1, w2 = [line.split(',') for line in f.read().splitlines()]

        w1_visited = visit(w1)
        w2_visited = visit(w2)

        # intersections of coordinates
        intersections = set(w1_visited.keys()).intersection(set(w2_visited.keys()))

        closest = min([abs(x) + abs(y) for (x, y) in intersections])
        print(closest)

        # Part 2
        lowest = min([w1_visited[intersection] + w2_visited[intersection] for intersection in intersections])
        print(lowest)


def visit(wire):
    step_deltas = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

    x = 0
    y = 0
    length = 0

    visited = {}

    for move in wire:
        direction = move[0]
        n = int(move[1:])

        step_delta = step_deltas[direction]

        for _ in range(n):
            x += step_delta[0]
            y += step_delta[1]
            length += 1
            visited[(x, y)] = length

    return visited


if __name__ == '__main__':
    run()
