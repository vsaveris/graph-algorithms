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
    vertices = ['A', 'B', 'C', 'D', 'E', 'S']   
    edges_with_lengths = {'A': [('S', 1), ('B', 1)], 
                          'B': [('A', 1), ('C', 1)],
                          'C': [('B', 1), ('S', 1)],
                          'D': [('E', 1), ('S', 1)],
                          'E': [('D', 1), ('S', 1)],
                          'S': [('E', 1), ('D', 1), ('C', 1), ('A', 1)]}
    
    # Create the graph object G = (V, E) given the V and E
    g = ga.Graph(vertices, edges_with_lengths)
    
    # Run BFS algorithm for the defined graph
    paths, cost = ga.GraphAlgorithms().bfs(G = (g.getVertices(), g.getEdges()), s = 'B')
    
    print('BFS shortest paths for the given graph, where starting node is \'B\':')
    start_node = 'B'
    for end_node in ['A', 'C', 'D', 'E', 'S']:
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
              
              
def demoDfs():
    '''
    Example code for the DFS algorithm.
    '''
    # Define the vertices and edges of the graph, in the structure 
    # the class Graph expects them
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']   
    edges_with_lengths = {'A': [('B', 1), ('E', 1)], 
                          'B': [('A', 1)],
                          'C': [('D', 1), ('G', 1), ('H', 1)],
                          'D': [('C', 1), ('H', 1)],
                          'E': [('A', 1), ('I', 1), ('J', 1)],
                          'F': [],
                          'G': [('C', 1), ('H', 1), ('K', 1)],
                          'H': [('D', 1), ('L', 1), ('C', 1), ('G', 1), ('K', 1)],
                          'I': [('E', 1), ('J', 1)],
                          'J': [('E', 1), ('I', 1)],
                          'K': [('G', 1), ('H', 1)],
                          'L': [('H', 1)]}
    
    # Create the graph object G = (V, E) given the V and E
    g = ga.Graph(vertices, edges_with_lengths)
    
    # Run DFS algorithm for the defined graph
    previsit, postvisit, ccnum  = ga.GraphAlgorithms().dfs(G = (g.getVertices(), g.getEdges()))
    
    print('DFS output for the given graph:')
    for node in vertices:
        print('node \'{:1}\': first_discovery_time = {:2},last_departure_time = {:2}, connected_component = {:2}'.\
              format(node, previsit[node], postvisit[node], ccnum[node]))
    
    for i in range(1, max(ccnum.values()) + 1):
        print('connected component ', i, ': ', [k for k,v in ccnum.items() if v == i], sep = '')
        

def demoBellmanFord():    
    '''
    Example code for the Bellman-Ford algorithm.
    '''
    # Define the vertices and edges of the graph, in the structure 
    # the class Graph expects them
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'S']   
    edges_with_lengths = {'A': [('E', 2)], 
                          'B': [('A', 1), ('C', 1)],
                          'C': [('D', 3)],
                          'D': [('E', -1)],
                          'E': [('B', -2)],
                          'F': [('A', -4), ('E', -1)],
                          'G': [('F', 1)],
                          'S': [('A', 10), ('G', 8)]}

    # Create the graph object G = (V, E) given the V and E
    g = ga.Graph(vertices, edges_with_lengths)
    
    # Run Bellman-Ford algorithm for the defined graph
    paths, cost = ga.GraphAlgorithms().bellmanFord(G = (g.getVertices(), g.getEdges()), l = g.getLengths(), s = 'S')

    # Back tracking the paths, we can get the shortest path for any destination node
    print('Bellman-Ford shortest paths for the given graph, where starting node is \'S\':')
    start_node = 'S'
    for end_node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
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


def demoKruskal():    
    '''
    Example code for the Kruskal algorithm.
    '''
    
    # Define the vertices and edges of the graph, in the structure 
    # the class Graph expects them
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']   
    edges_with_lengths = {'A': [('B', 5), ('C', 6), ('D', 4)], 
                          'B': [('A', 5), ('C', 1), ('D', 2)],
                          'C': [('A', 6), ('B', 1), ('D', 2), ('F', 3), ('E', 5)],
                          'D': [('A', 4), ('B', 2), ('C', 2), ('F', 4)],
                          'E': [('C', 5), ('F', 4)],
                          'F': [('D', 4), ('C', 3), ('E', 4)]}
                          
    # Create the graph object G = (V, E) given the V and E
    g = ga.Graph(vertices, edges_with_lengths)
    
    # Run Kruskal algorithm for the defined graph
    mst, total_weight = ga.MST().kruskal(G = g, w = g.getLengths())
     
    print('Kruskal Minimum Spanning Tree, for the given graph:')
    print('MST:', mst)
    print('MST total weight:', total_weight)
    

if __name__ == '__main__':

    # Parsing input arguments
    description_message = 'Demonstration script for the Graph Algorithms'
    epilog_message = 'Supported values for \'algorithm\' are (\'dfs\', \'bfs\', \'dijkstra\', \'bellman_ford\', \'kruskal\')\n\n' +\
                    'Example: \npython demoga.py -a dijkstra'
    args_parser = argparse.ArgumentParser(description = description_message, epilog = epilog_message,
                formatter_class=argparse.RawTextHelpFormatter)
    args_parser.add_argument('-a', action = 'store', required = True, help = 'demonstration algorithm',
                            choices = ('dfs', 'bfs', 'dijkstra', 'bellman_ford', 'kruskal'), metavar = 'algorithm')
    args = args_parser.parse_args()
      
    # Execute the requested demonstration code
    if args.a == 'bfs':
        demoBfs()
    elif args.a == 'dfs':
        demoDfs()
    elif args.a == 'dijkstra':
        demoDijkstra()
    elif args.a == 'bellman_ford':
        demoBellmanFord()
    elif args.a == 'kruskal':
        demoKruskal()
    else:
        print('Demonstration code for algorithm \'', args.a, '\' is missing', sep = '')
