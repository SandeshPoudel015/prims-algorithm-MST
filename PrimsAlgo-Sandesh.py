# -*- coding: utf-8 -*-
"""
Created on Mon May 17 23:51:37 2021

@author: HP
"""


# Prim's Algorithm in Python

import pandas as pd

INF = 9999999
print("This Python code implementation for Prim's Algorithm of Minimum Spanning Tree Generation is Created by Sandesh Poudel (9845176963), Pulchowk Campus.")
v = int(input("Enter the number of vertices: "))

# taking input from excel

csvin=pd.read_csv('DistanceMatrix-Sandesh.csv', header = None)

# creating an array of v*v size for adjacency matrix to represent graph

G = [[0 for i in range(v)] for j in range(v)]

for i in range(v):
    for j in range(v):
        G[i][j]=csvin.iloc[i,j]


# create a array to track selected vertex
# selected will become true otherwise false

selected =[False for i in range(v)]

# set number of edge to 0
no_edge = 0

# the number of egde in minimum spanning tree will be always less than(v - 1)
# choose 0th vertex and make it true

selected[0] = [True]

# print for edge and weight

print("Edge : Weight\n")
while (no_edge < v - 1):
    # For every vertex in the set S, find the all adjacent vertices
    #, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(v):
        if selected[i]:
            for j in range(v):
                if ((not selected[j]) and G[i][j]):
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1

print("^^Copy the above edge and distance values to your useful file format^^")
