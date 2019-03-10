import heapq
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.nodes = set(range(n))
        self.edges = defaultdict(list)
        self.distances = {}

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    h = [(0, initial)]
    path = {}

    nodes = set(graph.nodes)
    print(nodes)

    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        nodes.remove(min_node)

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                path[v] = min_node

    return visited, path

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge('A', 'B', 9)
    g.add_edge('B', 'C', 30)
    g.add_edge('B', 'D', 9)
    g.add_edge('C', 'A', 3)
    g.add_edge('D', 'C', 1)
    d = dijkstra(g, 'D')
    print(d)
