import pandas as pd


def export_bus_results(buses):
    data = []

    for bus in buses:
        data.append({
            "Bus ID": bus.bus_id,
            "Bus Type": bus.bus_type,
            "Voltage (pu)": bus.voltage,
            "Angle (deg)": bus.angle,
            "P Load": bus.p_load,
            "Q Load": bus.q_load,
            "P Generation": bus.p_gen,
            "Q Generation": bus.q_gen
        })

    df = pd.DataFrame(data)

    df.to_csv(
        "bus_results.csv",
        index=False
    )

    print("Results exported to bus_results.csv")