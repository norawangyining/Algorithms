import random
from scipy.spatial import distance
from collections import defaultdict
import sys 

n = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]


def Edist(x1,y1,x2,y2):
    a = (x1,y1)
    b = (x2,y2)
    edge = distance.euclidean(a, b)
    return edge
    
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self, v1, v2):
        if v1 == v2:
            self.graph[v1][v2] = 0
        else:
            self.graph[v1][v2] = random.uniform(0,1)
            self.graph[v2][v1] = self.graph[v1][v2]

    def addEdge2(self, v1, v2, weight):
        if v1 == v2:
            self.graph[v1][v2] = 0
        else:
            self.graph[v1][v2] = weight
            self.graph[v2][v1] = weight
        

  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minKey(self, key, mstSet): 
  
        # Initilaize min value 
        min = sys.maxsize 
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v
  
        return min_index 
  

    def primMST(self):  
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V 
        key[0] = 0 
        mstSet = [False] * self.V 
  
        parent[0] = -1
  
        for cout in range(self.V): 
            u = self.minKey(key, mstSet) 
            mstSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u
        totalweight = 0
        numnode = 0
        for i in range(1,self.V): 
            totalweight +=self.graph[i][ parent[i] ]
        return totalweight
    
weightlist =[]
weightlist2 =[]
def main():
    print("Average weight list result for TYPE 1")
    for z in n:
        g = Graph(z)
        for i in range(z):
            for j in range(z):
                g.addEdge(i, j)
        weights = 0
        for i in range(5):
            weights += g.primMST()
        weightlist.append(weights / 5)
    print(weightlist)
    print("Average weight list result for TYPE 2")
    for z in n:
        g = Graph(z)
        for i in range(z):
            for j in range(z):
                x = [random.uniform(0,1),random.uniform(0,1)]
                y = [random.uniform(0,1),random.uniform(0,1)]
                weight = Edist(x[0],y[0],x[1],y[1])
                g.addEdge2(i,j,weight)
        weights = 0
        for i in range(5):
            weights += g.primMST()
        aveweight= weights / 5
        weightlist2.append(aveweight)
        
    print(weightlist2)
    
if __name__ == '__main__':
   main()



