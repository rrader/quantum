import numpy as np

Q0 = np.array([1 + 0j, 0 + 0j])
Q1 = np.array([0 + 0j, 1 + 0j])


class Computer:
    def __init__(self, qubits, title=None):
        self.title = title
        self.history = []
        self.marks = []
        self.register = self.entangle(qubits)
        self.norm('Initial')

    def entangle(self, qubits):
        e = qubits[0]
        for q in qubits[1:]:
            e = np.kron(e, q)
        return e

    def __str__(self):
        s = []
        for q in self.register:
            s.append("{}, ".format(q))
        return "| {}>".format(''.join(s))

    def gate(self, matrix, name=None):
        self.register = (self.register @ matrix).flat
        self.norm(name)

    def norm(self, name):
        norm = np.sum(np.power(np.abs(self.register), 2)) ** 0.5
        self.register = self.register / norm
        self.history.append(self.register.copy())
        self.marks.append((name, self.register.copy()))

    def measure(self):
        probabilities = np.real(self.register) ** 2 + np.imag(self.register) ** 2
        n = len(self.register)
        states = np.random.choice(
            range(n), size=1, p=probabilities
        )
        return '{state:>0{digits}b}'.format(state=states[0], digits=int(np.log2(n)))

    def plot(self):
        pass


def repeat(bits_len):
    return np.identity(bits_len * 2)


I = np.matrix([
    [1, 0],
    [0, 1],
])

NOT = np.matrix([
    [0, 1],
    [1, 0],
])

H = np.matrix([
    [1, 1],
    [1, -1],
])
