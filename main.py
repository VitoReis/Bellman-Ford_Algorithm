import numpy as np
from igraph import *

def main():
        graph = Graph.Read_Ncol("myGraph.ncol", directed=True)
        dist = [np.inf] * graph.vcount()
        dist[graph.vs[0].index] = 0
        rout = [-1] * graph.vcount()

        for edge in graph.es:
            while dist[edge.target] > dist[edge.source] + edge['weight']:
                dist[edge.target] = dist[edge.source] + edge['weight']
                rout[edge.target] = edge.source

        print('*'*38)
        print('* Vertex * Distance * Route by index *')
        print('*' * 38)
        for vertex in graph.vs:
            print(f'\t{vertex["name"]}\t\t\t\t{dist[vertex.index]}\t\t\t\t{rout[vertex.index]}\t')
        print('*' * 38)

if __name__ == '__main__':
    main()