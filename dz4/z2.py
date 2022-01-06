import numpy as np
from z1 import multiply, pretty


def _parse(result):
    digits = result[:-4], result[-4:]

    parsed = [''] * len(digits)

    for i, digit in enumerate(digits):
        digit = "".join(list(map(str, digit)))
        parsed[i] = hex(int(digit, 2))[2:] if digit else ""

    return "".join(parsed)


def main(x, y, verbose=False):
    x = np.array(x)

    d = np.zeros((4, 8), 'int')
    for i in reversed(range(4)):
        x = np.roll(x, 1)

        if verbose:
            print()

        for x_i, y_i in zip(x, reversed(y)):
            result = multiply(x_i, y_i, poly_type='hex')

            if verbose:
                print(f"{x_i} * {y_i} = {pretty(result)}")

            d[i, 8 - result.shape[0]:] += result
            d[i] %= 2

    return _parse(np.sum(d, axis=0) % 2)


if __name__ == '__main__':
    print(f"-----------TEST--------------")
    print("result: ", main(["03", "01", "01", "02"], ["0B", "0D", "09", "0E"]))
    print(f"----------FINAL--------------")
    print("result: ", main(["C7", "E8", "C0", "43"], ["9C", "4E", "8D", "90"], verbose=True))
    # print("result: ", main(["F4", "D3", "31", "F8"], ["01", "D2", "61", "03"], verbose=True))
