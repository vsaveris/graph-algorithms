'''
File name: demoga.py
           Demonstration code for the GraphAlgorithms class (file: graphalgorithms.py).
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 16.10.2019

Python Version: 3.6
'''

import sys
sys.path.insert(1, '../')
import graphalgorithms as ga

'''
Example code for the Dijkstra's algorithm.
'''
# Define the vertices and edges of the graph, in the structure 
# the class Graph expects them
vertices = ['a', 'b', 'c', 'd', 'e', 'f', 's', 't']   
edges_with_lengths = {'s': [('a', 100), ('c', 90), ('e', 101)], 
                      'a': [('b', 100)],
                      'b': [('t', 5)],
                      'c': [('d', 105)],
                      'd': [('t', 10)],
                      'e': [('f', 101)],
                      'f': [('t', 1)]}

# Create the graph object G = (V, E) given the V and E
g = ga.Graph(vertices, edges_with_lengths)

# Run Dijkstra's algorithm for the defined graph
paths, cost = ga.GraphAlgorithms().dijkstra(G = (g.getVertices(), g.getEdges()), l = g.getLengths(), s = 's')

# Back tracking the paths, we can get the shortest path for any destination node
# Example: Get the shortest path from 's' to 't'
done = False
shortest_path = ['t']
current = 't'
while not done:
    shortest_path.insert(0, paths[current])       
    current = shortest_path[0]
    if current == 's':
        done = True

print('Dijkstra: Shortest path from \'s\' to \'t\' is: ', shortest_path, ' with cost ', cost['t'], sep = '')

'''
Example code for the BFS algorithm.
'''
# Define the vertices and edges of the graph, in the structure 
# the class Graph expects them
vertices = ['a', 'b', 'c', 'd', 'e', 'f', 's', 't']   
edges_with_lengths = {'s': [('a', 1), ('d', 1), ('e', 1)], 
                      'a': [('b', 1)],
                      'b': [('c', 1)],
                      'c': [('t', 1)],
                      'd': [('t', 1)],
                      'e': [('f', 1)],
                      'f': [('t', 1)]}

# Create the graph object G = (V, E) given the V and E
g = ga.Graph(vertices, edges_with_lengths)

# Run BFS algorithm for the defined graph
paths, cost = ga.GraphAlgorithms().bfs(G = (g.getVertices(), g.getEdges()), s = 's')

done = False
shortest_path = ['t']
current = 't'
while not done:
    shortest_path.insert(0, paths[current])       
    current = shortest_path[0]
    if current == 's':
        done = True

print('BFS: Shortest path from \'s\' to \'t\' is: ', shortest_path, ' with cost ', cost['t'], sep = '')
