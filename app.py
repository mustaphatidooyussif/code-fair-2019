"""
@author Mustapha Tidoo and Samuel Atule
"""
import csv 
from collections import defaultdict
from vertex import Vertex
import matplotlib.pyplot as plt 
import networkx as nx
from heapq import heappush, heappop
import math 
import sys 

class AirlineTransportation(object):
    """
    Optimal path from source to destination

    This algorithm uses the Dijskra's algorithm implementation to find the
    optimal path from a given source node to a destination node. 
    
    :param source: The source city and country. 
    :param destination: The destination city and country. 
    """
    def __init__(self, source, destination): #concat before passing
        self.airports_file = './data/airports.csv'
        self.routes_file = './data/routes.csv'
        self.airlines_file = './data/airlines.csv'
        self.source = source
        self.destination = destination
        self.source_code = None
        self.destination_code = None
        self.heap = []
        self.graph = self._generate_airline_graph()

    def _preprocess_data(self):
        pass 

    def _generate_airline_graph(self):
        """
        This function generates a graph representing the airline network. 
        :return :The graph representing the network. 
        """
        with open(self.airports_file, encoding="utf8") as airport_csv:
            airport_csv_reader = csv.reader(airport_csv, delimiter=',') 
            airport = {}
            for line in airport_csv_reader:
                airport[line[0]] = (line[6], line[7])  #airport lat and long cordinates
                city_country = line[2] + line[3]
                if  self.source.lower() == city_country.lower() or self.destination.lower() == city_country.lower():
                    airport[city_country.lower()] = line[0]   #airport id by city, country(helps to start Dijkstra)

        Vertex.cordinates = airport #initialize static variable

        with open(self.routes_file, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                #decode srcfrom file
                if Vertex.cordinates.get(self.source.lower(),None) == line[3]:
                    self.source_code = line[2]

                #decode dest from file
                if Vertex.cordinates.get(self.destination.lower(), None) == line[5]:
                    self.destination_code = line[4] 

                #generate graph for valid routes
                if line[3] in airport and  line[5] in airport:
                    Vertex(line[3], line[5], line[0],  line[2], line[7], line[4])  

        return Vertex.graph
        
    def _optimal_path(self):
        if(not self.source_code or not self.destination_code):
            print("Unsupported Request")
            exit(0)

        # dijsktra
        heappush(self.heap, (0, 0, self.source_code, 0)) #(status, distance, code, stops)

        # populate heap
        for key, val in self.graph.items():
            for item in val:
                heappush(self.heap, (item[3], item[1], item[0], item[2]))

        # optimal path
        optimal_path = []

        while len(self.heap) >= 1:
            # Extract the vertex with minimum distance value
            u = heappop(self.heap)

            not_dead_end = self.graph.get(u[2], None) 

            # check if destination is reached
            if u[0] != math.inf and u[2]  == self.destination_code:
                return optimal_path

            if not_dead_end:
                print(u)
                optimal_path.append(u)
                for v in not_dead_end:
                    print(v)
                    status_of_adj = float(u[0]) + float(v[1])
                    if u[0] != math.inf and status_of_adj < v[3]:
                        # self.heap.pop(self.heap.index((v[3], v[1], v[0], v[2])))
                        if (v[3], v[1], v[0], v[2]) in self.heap:
                            self.heap.remove(((v[3], v[1], v[0], v[2])))
                        # update status
                        heappush(self.heap, (status_of_adj, v[1], v[0], v[2]))
                    
                # print(optimal_path)
        # path doesn't exist
        return -1


if __name__ == "__main__":
    a = AirlineTransportation('AccraGhana', 'TamaleGhana')
    optimal_path = a._optimal_path()
    print(optimal_path)

