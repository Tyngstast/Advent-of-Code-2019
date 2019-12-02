import csv
import operator
import os


def run():
    basedir = os.path.abspath(os.path.dirname(__file__))
    in_file = os.path.join(basedir, 'program_alarm.in')

    with open(in_file) as f:
        reader = csv.reader(f)
        data = [int(x) for x in next(reader)]

        data[1] = 12
        data[2] = 2

        result = process(data)

        print(result[0])


def process(data):
    opcode_len = 4

    for i in range(0, len(data), opcode_len):
        opcode = data[i:i + opcode_len]

        if opcode[0] == 99:
            break

        operator = __get_operator(opcode[0])
        res = operator(data[opcode[1]], data[opcode[2]])
        data[opcode[3]] = res

    return data


def __get_operator(code):
    if code == 1:
        return operator.add
    elif code == 2:
        return operator.mul
    else:
        raise RuntimeError


if __name__ == '__main__':
    run()
