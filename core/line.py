class Line:
    def __init__(
        self,
        from_bus,
        to_bus,
        resistance,
        reactance,
        charging=0.0
    ):
        self.from_bus = from_bus
        self.to_bus = to_bus

        self.resistance = resistance
        self.reactance = reactance
        self.charging = charging

    def impedance(self):
        return complex(
            self.resistance,
            self.reactance
        )

    def admittance(self):
        return 1 / self.impedance()

    def __str__(self):
        return (
            f"Line {self.from_bus}"
            f" -> "
            f"{self.to_bus}"
        )