import numpy as np


class YBusBuilder:

    def __init__(self, buses, lines):
        self.buses = buses
        self.lines = lines
        self.n_bus = len(buses)

    def build(self):

        ybus = np.zeros(
            (self.n_bus, self.n_bus),
            dtype=complex
        )

        for line in self.lines:

            y = line.admittance()

            i = line.from_bus - 1
            j = line.to_bus - 1

            ybus[i, i] += y
            ybus[j, j] += y

            ybus[i, j] -= y
            ybus[j, i] -= y

        return ybus