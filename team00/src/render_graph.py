import networkx as nx
import matplotlib.pyplot as plt
import json

graph = nx.Graph()


def main():
    try:
        file = open("result.json", "r")
        json_object = json.load(file)
        file.close()
        graph.add_nodes_from(json_object.keys())

        for node, neighbors in json_object.items():
            for neighbor in neighbors:
                graph.add_edge(node, neighbor)

        nx.draw(graph, with_labels=True)
        plt.show()
    except FileNotFoundError:
        print('Database not found')


if __name__ == '__main__':
    main()
