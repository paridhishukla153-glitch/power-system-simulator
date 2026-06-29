import networkx as nx
import matplotlib.pyplot as plt


def plot_network(buses, lines):
    G = nx.Graph()

    for line in lines:
        G.add_edge(
            line.from_bus,
            line.to_bus
        )

    nx.draw(
        G,
        with_labels=True,
        node_size=3000,
        font_size=12
    )

    plt.title(
        "Power System Network"
    )

    plt.show()