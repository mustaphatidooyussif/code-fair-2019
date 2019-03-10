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
        self.graph = defaultdict(list)
        

    def add_edge(self, from_node, to_node, weight, stops, airline_code):
        self.graph[from_node].append((weight, to_node, stops, airline_code)) #(status, destination, stops, airline_code)

    def get_graph(self):
        return self.graph