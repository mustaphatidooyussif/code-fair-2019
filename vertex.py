"""
@author Mustapha Tidoo and Samuel Atule
"""
import sys
import math 
class Vertex(object):
    """
    Vertex class 

    This class represents an airport. 

    :param src_airport_id: The source airport ID.
    :param dst_airport_id: The destination airport ID.
    :param airline_code: The airline code.
    :param src_airport_code: The source airport code.
    :param stops: The number of stops.
    :param dst_airport_code: The destination airport code.
    :param status: The stutus of the vertex indicating visited or unvisited. 
    """

    graph = {}     #Adjacency list representation
    cordinates = {} #Airports positions e.g 293:(-23.3333, 4732379)

    def __init__(self, src_airport_id, dst_airport_id, airline_code, src_airport_code, stops, dst_airport_code, status = math.inf, airline_id = None):
        self.airline_id = airline_id    #may use to get airline name to report
        self.src_airport_id =  src_airport_id   #helps to get lat and long of source airport
        self.dst_airport_id = dst_airport_id
        self.airline_code = airline_code #to report 
        self.distance = self._haversine()  #calculate the distance between the adjancent airports
        if src_airport_code not in Vertex.graph:    #
            Vertex.graph[src_airport_code] = []
        Vertex.graph[src_airport_code].append([dst_airport_code, self.distance, stops, status])

    def _haversine(self):
        """
        Distance between two points on a greate circle

        This functions uses the Haversine formula to compute the distance between 
        two locations on a great circle. Haversine formula, d = 2 * r * arcsin(sqrt(h)), where
        h = sin2((lat2-lat1)/2) + cos(lon1) * cos(long2) * sin2((long2-long1)/2)

        @return :returns the distance between two points.
        """
        minh = 0
        maxh = 1
        lat1, lon1 = Vertex.cordinates[self.src_airport_id]  #source
        lat2, lon2 = Vertex.cordinates[self.dst_airport_id]  #origin
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
