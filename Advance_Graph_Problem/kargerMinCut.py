
import random


# graph representation as the adjacent list, fully connected graph
class Graph(object):
    def __init__(self):
        self.vertex = {}
        self.edges = []
        self.contracted_nodes = []

    def add_vertex(self, vn=None):
        assert type(vn) == int, "Vertex index must be integer!"
        if vn is None:
            self.vertex[len(self.vertex)] = []
        else:
            self.vertex[vn] = []

    def add_edge(self, u, v):
        try:
            if u not in self.vertex:
                raise ValueError
            self.vertex[u].append(v)
        except ValueError:
            self.add_vertex(u)
            self.vertex[u].append(v)

    def __str__(self):
        info_string = "Vertices:       ________Edges:_____________\n"
        print(info_string)
        ret_str = ''
        for vv in self.vertex.keys():
            ret_str += str(vv) + '   ' + str(self.vertex[vv]) + '\n'
        return ret_str

    def readGraphFromFile(self, file_name):
        # file format first column - vertices, other columns - connections
        with open(file_name) as rf:
            for line in rf:
                ln = line.strip().split()
                self.add_vertex(int(ln[0]))
                for v in ln[1:]:
                    self.add_edge(int(ln[0]), int(v))

    def kargerContraction(self):
        random.seed = 1
        while len(self.vertex) > 2:
            u = random.choice(list(self.vertex.keys()))
            w = random.choice(self.vertex[u])
            # merge w to u, connect all w edges to u, remove loops
            for node in self.vertex[w]:
                if node != u:
                    self.vertex[u].append(node)
                    self.vertex[node].append(u)
                self.vertex[node].remove(w)
            del self.vertex[w]
            print(self.vertex.keys())

if __name__ == "__main__":
    graph1 = Graph()
    graph1.add_vertex(3)
    graph1.add_edge(4, 3)
    graph1.add_edge(4, 5)
    graph1.add_edge(3, 5)
    print(graph1)
    file_name = 'kargerMinCut.txt'
    graph1.readGraphFromFile(file_name)
    graph1.kargerContraction()
    print(graph1)
    print(len(graph1.vertex[list(graph1.vertex.keys())[0]]))