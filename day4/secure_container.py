def run():
    lower_range = 367479
    upper_range = 893698

    c = 0

    for password in range(lower_range, upper_range):
        if is_valid(password):
            c += 1

    print(c)


def is_valid(password):
    arr = [int(x) for x in str(password)]

    mem = [0] * 10

    for i, d in enumerate(arr):
        if i < len(arr) - 1 and d > arr[i + 1]:
            return False

        mem[d] += 1

    # we have duplicate
    return 2 in mem


if __name__ == '__main__':
    run()
