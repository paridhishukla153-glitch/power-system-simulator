from core.bus import Bus
from core.line import Line
from core.generator import Generator


bus1 = Bus(
    bus_id=1,
    bus_type="Slack",
    voltage=1.06
)

bus2 = Bus(
    bus_id=2,
    bus_type="PQ",
    p_load=1.0,
    q_load=0.5
)

line12 = Line(
    from_bus=1,
    to_bus=2,
    resistance=0.02,
    reactance=0.06
)

gen1 = Generator(
    gen_id=1,
    bus_id=1,
    p_output=1.5
)

print(bus1)
print(bus2)

print(line12)

print(gen1)

print(
    "Line impedance:",
    line12.impedance()
)

print(
    "Line admittance:",
    line12.admittance()
)