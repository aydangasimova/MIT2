# from ps1.lecture_handout2 import *
from ps1.w3_ex2 import *


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return str(self.getSource()) + '->' + str(self.getDestination()) + ' (' + str(self.getWeight()) + ')'


my_edge = WeightedEdge("ABC", "BAC", 3)

print(my_edge)

# print(my_edge.getSource())