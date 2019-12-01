import os


def run():
    basedir = os.path.abspath(os.path.dirname(__file__))
    in_file = os.path.join(basedir, 'fuel_problem.in')

    with open(in_file) as f:
        data = [int(line.strip()) for line in f]

        result = fuel_requirements(data)

        print(result)


def fuel_requirements(data):
    total = 0
    for item in data:
        total += fuel_per_item(item, 0)

    return total


def fuel_per_item(item, total):
    fuel = (item // 3) - 2

    if fuel <= 0:
        return total

    total += fuel

    return fuel_per_item(fuel, total)


if __name__ == '__main__':
    run()
