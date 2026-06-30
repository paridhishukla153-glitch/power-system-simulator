import streamlit as st

from data.ieee3 import get_system as get_system_ieee3
from data.ieee5 import get_system as get_system_ieee5
from core.ybus import YBusBuilder
from core.nr_solver import NewtonRaphsonSolver

st.title("⚡ Power System Simulator")

st.write(
    "Python-based simulator for load flow analysis."
)

dataset = st.selectbox(
    "Select Test System",
    [
        "IEEE 3 Bus",
        "IEEE 5 Bus"
    ]
)

if st.button("Run Simulation"):
    if dataset == "IEEE 3 Bus":
        from data.ieee3 import get_system
    else:
        from data.ieee5 import get_system

    buses, lines = get_system()

    builder = YBusBuilder(
        buses,
        lines
    )

    ybus = builder.build()

    solver = NewtonRaphsonSolver(
        buses,
        ybus
    )

    P, Q = solver.calculate_power()
    mismatch = solver.calculate_mismatch()
    J = solver.build_jacobian()

    st.subheader("Active Power")
    st.write(P)

    st.subheader("Reactive Power")
    st.write(Q)

    st.subheader("Mismatch Vector")
    st.write(mismatch)

    st.subheader("Jacobian Matrix")
    st.write(J)

    st.success("Simulation Completed Successfully")