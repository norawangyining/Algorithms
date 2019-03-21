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
and report the average for each value of n. (It is possible, that depending on your implementation you won’t be able
to run it for the largest graphs. ) For each family of graphs, generate an appropriate figure that depicts your results.
Clearly label the axes and think carefully about the most effective representation (should it be a bar chart, line chart,
scatterplot, etc.). Also, interpret your results by giving (and plotting) two sample functions that characterize each
of your depicted results. For example, your answer might be f (n) = 2 log n, f (n) = 1.5 n, etc. Also, provide a few sentences of intuition for why the growth rate of your functions f(n) are reasonable. Do this for both types of graphs separately.
As per usual, submit both the written answer (and charts) as well as your code as part of your pdf submission in Gradescope.
You will work on this assignment as individuals. However, the same collaboration policy applies as with any other assignment; you may discuss with classmates as long as the conclusions you write are your own and you disclose your collaboration.
