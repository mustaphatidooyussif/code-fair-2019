"""
@author Mustapha Tidoo and Samuel Atule
"""
import csv 
from graph2 import Graph
import matplotlib.pyplot as plt 
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
        self.source_airline = None
        self.cordinates = self._airport_cordinates()  #get the airports cordinates
        self.graph = self._generate_graph()
        self.heap = []



    def _haversine(self, P, Q):
        """
        Distance between two points on a greate circle

        This functions uses the Haversine formula to compute the distance between 
        two locations on a great circle. Haversine formula, d = 2 * r * arcsin(sqrt(h)), where
        h = sin2((lat2-lat1)/2) + cos(lon1) * cos(long2) * sin2((long2-long1)/2)

        @return :returns the distance between two points.
        """
        minh = 0
        maxh = 1
        lat1, lon1 = P #source
        lat2, lon2 = Q  #origin
        lat1 = float(lat1)
        lat2 = float(lat2)
        lon1 = float(lon1)
        lon2 = float(lon2)
        radius = 6371 # km. Fix radius of the earth. 

        dlat = math.radians(lat2-lat1)  #source and destination latitude difference
        dlon = math.radians(lon2-lon1)  #source and destination longitude difference
        h = math.pow(math.sin(dlat/2), 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) \
           * math.pow(math.sin(dlon/2), 2)

        #Ensure that h does not exceed 1 due to a floating point error (d is only real for h from 0 to 1).
        h = minh if h < minh else maxh if h > maxh else h
        d =  2 * radius * math.asin(math.sqrt(h)) 
        return d

    def _airport_cordinates(self):

        with open(self.airports_file, encoding="utf8") as airport_csv:
            airport_csv_reader = csv.reader(airport_csv, delimiter=',') 
            airport = {}
            for line in airport_csv_reader:
                airport[line[0]] = (line[6], line[7])  #airport lat and long cordinates
                city_country = line[2] + line[3]

                if  self.source.lower() == city_country.lower(): 
                    airport[city_country.lower()] = line[0]  

                if self.destination.lower() == city_country.lower():
                    airport[city_country.lower()] = line[0]
        return airport

    def _generate_graph(self):
        """
        This function generates a graph representing the airline network. 
        :return :The graph representing the network. 
        """
        with open(self.routes_file, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            g = Graph()
            for line in csv_reader:
                #decode srcfrom file
                src_airport_cord = line[3]
                dst_airport_cord = line[5]
                if src_airport_cord in self.cordinates and dst_airport_cord in self.cordinates:
                    d = self._haversine(self.cordinates[src_airport_cord], self.cordinates[dst_airport_cord]) 

                    #add_edge(from_node, to_node, weight, stops, airline_code)
                    g.add_edge(line[2], line[4], d, line[7], line[0]) 

                    #decode src from file
                    if self.cordinates.get(self.source.lower(), None) == line[3]:
                        self.source_code = line[2]
                        self.source_airline = line[0]

                    #decode dest from file
                    if self.cordinates.get(self.destination.lower(), None) == line[5]:
                        self.destination_code = line[4] 

            return g

    def dijsktra(self):
        """
        Finding optimal path

        This function implememnts the dijsktra algoritms. 
        :return : it returns tuples containing the total distance, source and destination airport
                  available, othwerise raises an exception. 
        """
        if self.source_code is None or self.destination_code is None:
            print("Error: Unsupported Request")
            exit(0)

        #(status, destination, stops, airline_code) e.g (333.5901828627264, 'URC', '0', 'CZ')
        visited = {self.source_code: 0}
        heappush(self.heap, (0, self.source_code))
        path = []
        airlines_used = {self.source_code: 'No airline'}
        stops = {"total": 0}
        nodes = set(self.graph.nodes)
        while nodes and self.heap:
            current_weight, min_node = heappop(self.heap)
            try:
                while min_node not in nodes:
                    current_weight, min_node = heappop(self.heap)
            except IndexError:
                break

            nodes.remove(min_node)
            path.append(min_node)
            if min_node == self.destination_code:
                return visited, path, airlines_used, stops

            for v in self.graph.edges[min_node]:
                weight = current_weight + self.graph.distances[min_node, v]
                if v not in visited or weight < visited[v]:
                    visited[v] = weight
                    airlines_used[v] = self.graph.airlines[min_node, v]
                    stops[v] = self.graph.stops[min_node, v]  #stops
                    stops['total'] = stops.get('total') + int(self.graph.stops[min_node, v]) #count stops
                    heappush(self.heap, (weight, v))

        return (0, 0, 0, 0)

if __name__ == "__main__":
    input_file =  sys.argv[1]
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        input_value = []
        for line in csv_reader:
            line = ''.join(line)
            line = line.replace(" ", "")
            input_value.append(line)

    a = AirlineTransportation(input_value[0], input_value[1])
    destination_code = a.destination_code
    distance, path, airline, stops = a.dijsktra()

    for i in range(len(path)-1):
        # airline code, from airport, to airport, stops
        print(airline[path[i+1]], path[i], path[i+1], stops[path[i+1]])

    # total distance
    print(distance[destination_code])

    print(stops.get('total'))

