"""
@author Mustapha Tidoo and Samuel Atule
"""
import sys
import math 
class Graph(object):
    """
    Graph class 

    This class represents an airport. 

    :param src_airport_id: The source airport ID.
    :param dst_airport_id: The destination airport ID.
    :param airline_code: The airline code.
    :param src_airport_code: The source airport code.
    :param stops: The number of stops.
    :param dst_airport_code: The destination airport code.
    :param status: The stutus of the Vertex indicating visited or unvisited. 
    """

    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dst, weight, stops, airline_code):
        if src not in self.graph:    #
            self.graph[src] = []
        self.graph[src].append((weight, dst, stops, airline_code)) #(status, destination, distance, stops, airline_code)

    def get_graph(self):
        return self.graph