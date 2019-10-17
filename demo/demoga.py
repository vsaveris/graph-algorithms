'''
File name: demoga.py
           Demonstration code for the GraphAlgorithms class (file: graphalgorithms.py).
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 16.10.2019

Python Version: 3.6
'''

import sys, argparse
sys.path.insert(1, '../')
import graphalgorithms as ga


def demoDijkstra():
    '''
    Example code for the Dijkstra's algorithm.
    '''
    # Define the vertices and edges of the graph, in the structure 
    # the class Graph expects them
    vertices = ['A', 'B', 'C', 'D', 'E']   
    edges_with_lengths = {'A': [('B', 4), ('C', 2)], 
                          'B': [('D', 2), ('E', 3), ('C', 3)],
                          'C': [('B', 1), ('E', 5), ('D', 4)],
                          'D': [],
                          'E': [('D', 1)]}

    # Create the graph object G = (V, E) given the V and E
    g = ga.Graph(vertices, edges_with_lengths)
    
    # Run Dijkstra's algorithm for the defined graph
    paths, cost = ga.GraphAlgorithms().dijkstra(G = (g.getVertices(), g.getEdges()), l = g.getLengths(), s = 'A')
    
    # Back tracking the paths, we can get the shortest path for any destination node
    print('Dijkstra shortest paths for the given graph, where starting node is \'A\':')
    start_node = 'A'
    for end_node in ['B', 'C', 'D', 'E']:
        done = False
        shortest_path = [end_node]
        current = end_node
        while not done:
            shortest_path.insert(0, paths[current])       
            current = shortest_path[0]
            if current == start_node:
                done = True
        
        print('Shortest path from \'', start_node, '\' to \'', end_node, '\' is: ', shortest_path, 
              ' with cost ', cost[end_node], sep = '')
    

def demoBfs():
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


if __name__ == '__main__':

    # Parsing input arguments
    description_message = 'Demonstration script for the GraphAlgorithms class'
    epilog_message = 'Supported values for \'algorithm\' are (\'bfs\',\'dijkstra\')\n\n' +\
                    'Example: \npython demoga.py -a dijkstra'
    args_parser = argparse.ArgumentParser(description = description_message, epilog = epilog_message,
                formatter_class=argparse.RawTextHelpFormatter)
    args_parser.add_argument('-a', action = 'store', required = True, help = 'demonstration algorithm',
                            choices = ('bfs', 'dijkstra'), metavar = 'algorithm')
    args = args_parser.parse_args()
      
    # Execute the requested demonstration code
    if args.a == 'bfs':
        demoBfs()
    elif args.a == 'dijkstra':
        demoDijkstra()
    else:
        print('Demonstration code for algorithm \'', args.a, '\' is missing', sep = '')
