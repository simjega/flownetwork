import sys
from util import parse, makeAbsolutePath
from os import getcwd
from edge import Edge
from graph import Graph
from flow_network import FlowNetwork


def setup(path):
    v, e = parse(path)
    g = Graph(v, e)
    f = FlowNetwork(g)
    return f


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        path = makeAbsolutePath(args[1])
    else:
        path = getcwd() + '/testFN.csv'
    network = setup(path)

    max_flow = network.fordFulkerson()
    print max_flow
