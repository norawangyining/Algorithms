# Algorithms

* Minimum Spanning Trees 
Problem: 
In this programming problem, we will be considering MSTs on complete, undirected graphs.
A graph with n vertices is complete if all possible 􏲂n􏲃 edges are present in the graph. Consider the following two 2
types of graphs:

• Complete graphs on n vertices, where the weight of each edge is a real number chosen uniformly at random
from [0, 1].

• Complete graphs on n vertices, where the vertices are points chosen uniformly at random inside the unit square. (That is, the points are (x, y), with x and y each a real number chosen uniformly at random from [0, 1].) The weight of an edge is the Euclidean distance between its endpoints.

Your goal is to determine how the average weight of the minimum spanning tree grows as a function of n for each of these families of graphs. You will need to implement an MST algorithm and procedures that generate the appropriate random graphs. Run your program on at least five random graph instances for

n = 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192

and report the average for each value of n. 
