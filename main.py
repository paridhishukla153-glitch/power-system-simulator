from core.ybus import YBusBuilder
from core.nr_solver import NewtonRaphsonSolver
from visualization.network_plot import plot_network
from data.ieee5 import get_system
from utils.export_results import export_bus_results


# Load IEEE 3 Bus System
buses, lines = get_system()


# Build Y-Bus Matrix
builder = YBusBuilder(
    buses,
    lines
)

ybus = builder.build()


# Initialize Newton-Raphson Solver
solver = NewtonRaphsonSolver(
    buses,
    ybus
)


# Calculate Active and Reactive Power
P, Q = solver.calculate_power()

print("Active Power:")
print(P)

print()

print("Reactive Power:")
print(Q)

print()


# Calculate Mismatch Vector
mismatch = solver.calculate_mismatch()

print("Mismatch Vector:")
print(mismatch)

print()


# Build Jacobian Matrix
J = solver.build_jacobian()

print("Jacobian Matrix:")
print(J)

print()


# Visualize Network
plot_network(
    buses,
    lines
)

export_bus_results(buses)