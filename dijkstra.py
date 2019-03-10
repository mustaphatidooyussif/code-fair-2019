import heapq
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_edge(self, from_node, to_node, distance):
        self.nodes.add(from_node)
        self.nodes.add(to_node)
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance


def dijkstra(graph, initial, target):
    visited = {initial: 0}
    h = [(0, initial)]
    path = []

    nodes = set(graph.nodes)
    print(graph.edges)
    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        nodes.remove(min_node)
        path.append(min_node)
        
        if min_node == target:
            return visited, path

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                
            
    return (0, 0)

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge('A', 'B', 7)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 9)
    g.add_edge('C', 'A', 8)
    g.add_edge('C', 'D', 6)
    g.add_edge('D', 'E', 2)
    g.add_edge('D', 'A', 3)
    d, p = dijkstra(g, 'A', 'D')
    # print(d)
    # print()
    # print(p)
