from core.bus import Bus
from core.line import Line


def get_system():

    buses = [
        Bus(
            1,
            "Slack",
            voltage=1.06
        ),

        Bus(
            2,
            "PQ",
            voltage=1.0,
            p_load=1.0,
            q_load=0.5
        ),

        Bus(
            3,
            "PQ",
            voltage=1.0,
            p_load=0.8,
            q_load=0.3
        )
    ]

    lines = [
        Line(
            1,
            2,
            0.02,
            0.06
        ),

        Line(
            1,
            3,
            0.08,
            0.24
        ),

        Line(
            2,
            3,
            0.06,
            0.18
        )
    ]

    return buses, lines