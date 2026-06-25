class Generator:
    def __init__(
        self,
        gen_id,
        bus_id,
        p_output,
        q_output=0.0,
        v_setpoint=1.0
    ):
        self.gen_id = gen_id
        self.bus_id = bus_id

        self.p_output = p_output
        self.q_output = q_output

        self.v_setpoint = v_setpoint

    def __str__(self):
        return (
            f"Generator {self.gen_id}"
            f" on Bus {self.bus_id}"
        )