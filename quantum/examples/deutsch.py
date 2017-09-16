from collections import Counter

import numpy as np

from quantum.gates import Computer, I, NOT, H, Q0
from quantum.plot_quantum import plot

F1 = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])
F2 = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])
F3 = np.matrix([
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])
F4 = np.matrix([
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])


def is_constant(oracle):
    c = calculate(oracle, 'name')

    # print(c)
    v = c.measure()
    if v[0] == '1':
        return True
    return False


def calculate(oracle, name):
    c = Computer([Q0, Q0], name)
    c.gate(np.kron(I, NOT), 'NOT[2]')
    c.gate(np.kron(H, I), 'Hadamard[1]')
    c.gate(np.kron(I, H), 'Hadamard[2]')
    c.gate(oracle, 'Oracle')
    c.gate(np.kron(H, H), 'Hadamard[1,2]')
    c.gate(np.kron(I, NOT), 'NOT[2]')
    return c


def main(oracle):
    v = []
    for i in range(10):
        v.append(is_constant(oracle))
    c = Counter(v)
    print(c)
    print('Constant' if c.most_common(1)[0][0] else 'Balanced')
    print('-------------')


if __name__ == "__main__":
    main(F1)
    main(F2)
    main(F3)
    main(F4)

    c = calculate(F2, 'Deutsch F2')
    plot(c)
