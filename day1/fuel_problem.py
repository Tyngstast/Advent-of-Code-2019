import os


def run():
    basedir = os.path.abspath(os.path.dirname(__file__))
    in_file = os.path.join(basedir, 'fuel_problem.in')

    with open(in_file) as f:
        data = [int(line.strip()) for line in f]

        result = fuel_requirements(data)

        print(result)


def fuel_requirements(data):
    sum = 0
    for val in data:
        sum += calc_fuel_helper(val, 0)

    return sum


def calc_fuel_helper(data, sum):
    res = (data // 3) - 2

    if res <= 0:
        return sum

    sum += res

    return calc_fuel_helper(res, sum)


if __name__ == '__main__':
    run()
