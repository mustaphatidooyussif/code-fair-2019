"""
@author Mustapha Tidoo and Samuel Atule
"""
import csv 
from collections import defaultdict
from vertex import Vertex

class AirlineTransportation(object):

    def __init__(self, input_filename):
        self.airports_file = './data/airports.csv'
        self.routes_file = './data/routes.csv'
        self.airlines_file = './data/airlines.csv'
        self.input_filename = input_filename

    def _preprocess_data(self):
        pass 

    def _generate_airline_graph(self):
        with open(self.airports_file, encoding="utf8") as airport_csv:
            airport_csvreader = csv.reader(airport_csv, delimiter=',') 
            cordinates = {}
            for line in airport_csvreader:
                cordinates[line[0]] = (line[6], line[7])

        with open(self.routes_file, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                # Vertex(line[0], line[3], line[1], line[2], line[4])
                pass 


if __name__ == "__main__":
    a = AirlineTransportation('file.txt')
    a._generate_airline_graph()

