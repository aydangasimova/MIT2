from ps1.lecture3_handout import *
import re

nodes = []

nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()

for n in nodes:
    print(n)
    g.addNode(n)


for j in range(len(nodes)):
    for i in range(len(nodes)):
        if nodes[i].getName() == nodes[j].getName():
            break
        else:
            if nodes[j].getName()[0] == nodes[i].getName()[0] or nodes[j].getName()[-1] == nodes[i].getName()[-1]:
                g.addEdge(Edge(nodes[j], nodes[i]))
