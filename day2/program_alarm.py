import csv
import operator
import os


def run():
    basedir = os.path.abspath(os.path.dirname(__file__))
    in_file = os.path.join(basedir, 'program_alarm.in')

    with open(in_file) as f:
        reader = csv.reader(f)
        data = [int(x) for x in next(reader)]

        # 12 2 : 5482655
        # 12 0 : 5482653

        # idx 2 : add

        # 11 0 : 5098653. 5482653 (12) - 5098653 (11) = 384000
        # 13 0 : 5866653. 5866653 (13) - 5482653 (12) = 384000

        # Wanted is 19690720. 19690720 / 384000 = 51,277916667
        # 51 0 :    20458653
        # 49 0 :    19690653. 19690720 - 19690653 = 67

        data[1] = 49
        data[2] = 67

        result = process(data)

        print(result[0])


def process(data):
    opcode_len = 4

    for i in range(0, len(data), opcode_len):
        opcode = data[i:i + opcode_len]

        if opcode[0] == 99:
            break

        op = __get_operator(opcode[0])
        op_res = op(data[opcode[1]], data[opcode[2]])
        data[opcode[3]] = op_res

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
