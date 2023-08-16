import random
import sys

def ParseGraph(filename):
    vertices = []
    edges = set([])

    for line in open(filename):
        fields = [int(f) for f in line.split()]
        vertex = fields.pop(0)
        incident = [tuple(sorted([vertex, f])) for f in fields]
        vertices.append(vertex)
        edges.update(incident)

    return vertices, list(edges)

def RandomContraction(vertices, edges):
    while len(vertices) > 2:
        edge = random.choice(edges)
        a, b = edge
        vertices.remove(b)
        new_edges = []
        for e in edges:
            if e == edge:
                continue
            if b in e:
                if e[0] == b:
                    other = e[1]
                else:
                    other = e[0]
                e = tuple(sorted([a, other]))
            new_edges.append(e)
        edges = new_edges

    return vertices, edges

# Replace 'filename' with the actual path to your graph file
filename = 'kargerMinCut.txt'

vertices, edges = ParseGraph(filename)

minimum = sys.maxsize
for i in range(0, 1000):
    v, e = RandomContraction(vertices[:], edges[:])
    #print(v, len(e))
    if len(e) < minimum:
        minimum = len(e)

print("min cut: %d" % minimum)
