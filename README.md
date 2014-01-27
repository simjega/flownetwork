FlowNetwork

This is a simple toy flow network written in python

It includes:
* Classes for edges, graphs and networks
* A parser that can read in a flow network graph
* An implementation of Ford-Fulkerson (Edmonds–Karp BFS augmenting path search)

main.py can parse and call all functions

Usage: 
```
cd path/to/repo
python main.py "path/to/csv/file"
```

CSV file format:
```
v
i,j,C_ij
i,j,C_ij
...
```

where: 
* v = # of vertices
* i,j = indices of vertices
* C_ij = capacity of edge going from vertex i to vertex j

