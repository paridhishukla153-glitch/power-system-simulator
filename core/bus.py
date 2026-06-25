class Bus:
    def __init__(
        self,
        bus_id,
        bus_type,
        voltage=1.0,
        angle=0.0,
        p_load=0.0,
        q_load=0.0,
        p_gen=0.0,
        q_gen=0.0
    ):
        self.bus_id = bus_id
        self.bus_type = bus_type
        self.voltage = voltage
        self.angle = angle

        self.p_load = p_load
        self.q_load = q_load

        self.p_gen = p_gen
        self.q_gen = q_gen

    def net_active_power(self):
        return self.p_gen - self.p_load

    def net_reactive_power(self):
        return self.q_gen - self.q_load

    def __str__(self):
        return (
            f"Bus {self.bus_id} | "
            f"Type: {self.bus_type} | "
            f"V={self.voltage:.3f} pu | "
            f"Angle={self.angle:.3f} deg"
        )