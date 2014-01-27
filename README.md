FlowNetwork

This is a simple toy flow network written in python

It includes:
* Classes for edges, graphs and networks
* A parser that can read in a flow network graph
* An implementation of Ford-Fulkerson (Edmonds–Karp BFS augmenting path search)

main.py can parse and call all functions

Usage: 
    cd path/to/repo
    python main.py "path/to/csv/file"


CSV file format:
    v
    i,j,C_i,j
    i,j,C_i,j
    ...

where v = # of vertices
i,j = indices of vertices and the capacity of connection going from vertex i to vertex j
