import numpy as np


class NewtonRaphsonSolver:

    def __init__(self, buses, ybus):
        self.buses = buses
        self.ybus = ybus
        self.n_bus = len(buses)

    def calculate_power(self):
        """
        Calculate active and reactive power injections
        at every bus.
        """

        P = np.zeros(self.n_bus)
        Q = np.zeros(self.n_bus)

        # Voltage magnitudes
        V = np.array([bus.voltage for bus in self.buses])

        # Convert degrees to radians
        theta = np.radians(
            [bus.angle for bus in self.buses]
        )

        # Separate conductance and susceptance
        G = self.ybus.real
        B = self.ybus.imag

        for i in range(self.n_bus):
            for j in range(self.n_bus):

                angle_diff = theta[i] - theta[j]

                P[i] += (
                    V[i]
                    * V[j]
                    * (
                        G[i, j] * np.cos(angle_diff)
                        +
                        B[i, j] * np.sin(angle_diff)
                    )
                )

                Q[i] += (
                    V[i]
                    * V[j]
                    * (
                        G[i, j] * np.sin(angle_diff)
                        -
                        B[i, j] * np.cos(angle_diff)
                    )
                )

        return P, Q

    def calculate_mismatch(self):
        """
        Calculate mismatch vector:
        ΔP and ΔQ
        """

        P_calc, Q_calc = self.calculate_power()

        delta_P = []
        delta_Q = []

        for i, bus in enumerate(self.buses):

            # Skip slack bus
            if bus.bus_type == "Slack":
                continue

            # Specified active power
            P_spec = bus.p_gen - bus.p_load

            # Active power mismatch
            delta_P.append(
                P_spec - P_calc[i]
            )

            # Only PQ buses use reactive mismatch
            if bus.bus_type == "PQ":

                Q_spec = bus.q_gen - bus.q_load

                delta_Q.append(
                    Q_spec - Q_calc[i]
                )

        mismatch = np.concatenate(
            (
                np.array(delta_P),
                np.array(delta_Q)
            )
        )

        return mismatch

    def build_jacobian(self):
        """
        Create Jacobian matrix structure.
        """

        n_pq = sum(
            1 for bus in self.buses
            if bus.bus_type == "PQ"
        )

        n_non_slack = sum(
            1 for bus in self.buses
            if bus.bus_type != "Slack"
        )

        size = n_non_slack + n_pq

        J = np.zeros((size, size))

        return J