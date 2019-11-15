from ps1.w3_ex2 import *

# create a list of nodes objects

nodes = []

nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

# initiate empty graph

g = Graph()

# add nodes to graph

print("the nodes are \n")
for n in nodes:
    print(n)
    g.addNode(n)

# add edges to graph

for j in range(len(nodes)):
    for i in range(len(nodes)):
        if nodes[i].getName() == nodes[j].getName():
            break
        else:
            if nodes[j].getName()[0] == nodes[i].getName()[0] or nodes[j].getName()[-1] == nodes[i].getName()[-1]:
                g.addEdge(Edge(nodes[j], nodes[i]))

print("\n the graph is: \n")
print(g)


# edit the print function to print the index of the node rather than its name or object name


def printPath(path): # is just used to print the path in a pretty way
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        # print(str(path[i]))
        result += str(nodes.index(g.getNode(str(path[i]))))
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start]
    if toPrint:  # we only print what the algorithm is up to when we specify it as a parameter in the function.
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest


# here we only need the DFS function because we are not interested in the shortest path found but in the first path found

DFS(g, nodes[3], nodes[1], [], None, toPrint = True)
