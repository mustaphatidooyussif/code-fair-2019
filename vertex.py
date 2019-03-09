"""
@author Mustapha Tidoo and Samuel Atule
"""

import math 
class Vertex(object):
    """
    Vertex class 

    This class represents an airport. 

    @param airline_id:
    @param airport_id:
    @param airline_code:
    @param src_airport_code:
    @param dst_airport_code:
    """

    graph = {}     #Adjacency list representation
    cordinates = {} #Airports positions e.g 293:(-23.3333, 4732379)

    def __init__(self, airline_id, src_airport_id, dst_airport_id, airline_code, src_airport_code, stops, dst_airport_code, status = math.inf):
        self.airline_id = airline_id    #may use to get airline name to report
        self.src_airport_id =  src_airport_id   #helps to get lat and long of source airport
        self.dst_airport_id = dst_airport_id
        self.airline_code = airline_code #to report 
        self.distance = self._havsersine()  #calculate the distance between the adjancent airports
        if src_airport_code not in Vertex.graph:    #
            Vertex.graph[src_airport_code] = []
        Vertex.graph[src_airport_code].append([dst_airport_code, self.distance, stops, status])

    def _havsersine(self):
        P = Vertex.cordinates[self.src_airport_id]
        Q = Vertex.cordinates[self.dst_airport_id]
        # calculate haversine of p and q 
        hav = 1 
        return hav

    



