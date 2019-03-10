"""
@author Mustapha Tidoo and Samuel Atule
"""
import sys
import math 
from collections import defaultdict

class Graph(object):
    """
    Graph class 

    This class represents an airport. 

    :param airline_code: The airline code.
    :param from_node: The source airport code.
    :param stops: The number of stops.
    :param to_node: The destination airport code.
    :param status: The stutus of the Vertex indicating visited or unvisited. 
    """

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.stops = {}
        self.airlines = {}

    def add_edge(self, from_node, to_node, weight, stops, airline_code):
        self.nodes.add(from_node)
        self.nodes.add(to_node)
        self.edges[from_node].append(to_node) #(status, destination, stops, airline_code)
        self.distances[from_node, to_node] = weight
        self.stops[from_node, to_node] = stops
        self.airlines[from_node, to_node] = airline_code
