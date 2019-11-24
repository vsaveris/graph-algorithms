'''
File name: graphalgorithms.py
           Graph Algorithms implementations. Contains the following classes:
           - GraphAlgorithms: Graph algorithms implementation class. 
           - Graph: Graph data structure. Supplementary class.
           - UpdatablePriorityQueue: Extends PriorityQueue python class.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 17.10.2019

Python Version: 3.6
'''

from queue import PriorityQueue, Queue

class Graph(object):
    '''
    Graph G = (V, E) object, where V vertices and E edges.

    Args:
        vertices (list)   : A list containing the nodes of the graph.
                            i.e. ['a', 'b', 'c', 'd']
                            
        edges_with_lengths (dictionary): A dictionary containing the edges of the graph with
                            their lengths.
                            i.e. 
                            {'a': [('b', 10), ('c', 20)], 
                             'd': [('a': 30)]}
                            node 'a' is connected with 'b' (length 10) and 'c' (length 20)
                            node 'd' is connected with 'a' (length 30)
                            The above is an example of directed graph. The same as undirected
                            would be:
                            {'a': [('b', 10), ('c', 20), ('d', 30)], 
                             'd': [('a': 30)],
                             'b': [('a',10)], 
                             'c': [('a',20)]}

    Attributes:
        __vertices (list)     : Where vertices are stored.
                                Copy the value of the vertices.
        __edges (dictionary)  : Where edges are stored.
                                Taken from the edges_with_lengths: i.e. {'a': ['b', 'c'], 'd': ['a']}
        __lengths (dictionary): Where lengths are stored.
                                Taken from the edges_with_lengths: i.e. {'a': {'b': 10, 'c': 20}, 'd': {'a': 30}}
                                
    Methods:
        getVertices() : Returns the vertices of the graph (V)
        getEdges()    : Returns the edges of the graph (E)
        getLengths()  : Returns the length of the edges (le)
    '''
    
    def __init__(self, vertices, edges_with_lengths):
        
        # Store vertices
        self.__vertices = vertices
            
        # If a vertex is missing from the edges dictionary then add it with none connected nodes.
        for v in self.__vertices:
            try:
                edges_with_lengths[v]
            except:
                edges_with_lengths[v] = []
                
        # Store edges and lengths
        self.__edges = {}
        self.__lengths = {}
        for key, value in zip(edges_with_lengths.keys(), edges_with_lengths.values()):
            self.__edges[key] = [e[0] for e in value]
            self.__lengths[key] = {e[0]: e[1] for e in value}
            
    
    def getVertices(self):
        '''
        Returns the vertices of the graph (V from the G = (V, E))

        Args:
            -

        Raises:
            -

        Returns:
            vertices (list): The graph nodes.
            See class docstring for the list details.
        '''
        
        return self.__vertices
        
        
    def getEdges(self):
        '''
        Returns the edges of the graph (E from the G = (V, E)).
        
        Args:
            -

        Raises:
            -

        Returns:
            edges (dictionary): The graph edges.
            See class docstring for the dictionary details.
        '''
    
        return self.__edges
        
        
    def getLengths(self):
        '''
        Returns the edges lengths of the graph (le from the G = (V, E)).
        
        Args:
            -

        Raises:
            -

        Returns:
            lengths (dictionary): The graph edges with their lengths.
            See class docstring for the dictionary details.
        '''
    
        return self.__lengths
        
        

class UpdatablePriorityQueue(PriorityQueue):
    '''
    Updatable priority queue. Extends the PriorityQueue python class.

    Args:
        maxsize (int, default = 0): The maximum size of the queue. If zero, 
                                    the queue is not bounded.

    Attributes:
        -
        
    Methods:
        updatePriority(self, key, new_priority): Updates the priority of the key item. 

    Note: Each item in the queue has the type of (priority, key)
    '''
    
    def __init__(self, maxsize = 0):
    
        # Call the constructor of the parent class.
        super().__init__(maxsize)

    
    def updatePriority(self, key, new_priority):
        '''
        Updates the priority of an item in the queue, in time O(n).

        Args:
            key (string): The item to be updated.
            new_priority (number): The new priority of the key item.

        Raises:
            -

        Returns:
            edges (dictionary)
        '''

        # The updated queue
        updated_queue = PriorityQueue()

        # Copy the items to the updated queue, by modifying the priority of the 
        # requested one.
        while not self.empty():
            item = self.get()

            if item[1] != key:  
                updated_queue.put(item)
            else:
                updated_queue.put((new_priority, key))

        # Put the updated items in the original queue. Copy was not used for keeping
        # the object unchanged.
        while not updated_queue.empty():
            self.put(updated_queue.get())
        
    
class GraphAlgorithms(object):
    '''
    Graph algorithms implementation. See methods for the implemented algorithms.

    Args:
        -

    Attributes:
        -
        
    Methods:
        dijkstra(self, G, l, s) : Implementation of the Dijkstra's algorithm.
        bfs(self, G, s): Implementation of the Breadth-first search algorithm.
        dfs(self, G): Implementation of the Depth-first search algorithm.
        bellmanFord(self, G, l, s): Implementation of the Bellman-Ford algorithm.
    '''

    def __init__(self):
  
        pass
        
        
    def dijkstra(self, G, l, s):
        '''
        Dijkstra's algorithm for finding the shortest paths in a graph.
        Returns the shortest paths from node 's' to any other node together with the
        related path cost.

        Args:
            G (tuple(list,dictionary)): The graph G = (V,E).
            l (dictionary): The edges lengths of the graph G = (V,E).
            s (string): Starting node.

        Raises:
            'Non positive edge length found.' : Edge lengths in the Dijkstra's 
                                                algorithm should be positives numbers.

        Returns:
            previous (dictionary): The previous data structure of the algorithm.
            distance (dictionary): The distance data structure of the algorithm.
            
            Backtracking the previous structure we can get the shortest path from
            the starting node to any other node. Path cost is the distance[terminating_node].
        '''
    
        # Initializations
        V = G[0]
        E = G[1]
        # Initialize distances as defined in the algorithm
        distance = {key: float('inf') for key in V}
        distance[s] = 0
        
        # Initialize the previous structure as defined in the algorithm
        previous = {key: None for key in V}
        
        # Updatable priority queue contains items of the type (priority, node)
        priority_queue = UpdatablePriorityQueue()
        # Initialize the queue as defined in the algorithm
        for v in V:
            priority_queue.put((distance[v], v))
        
        # Loop until all the nodes are explored
        while not priority_queue.empty():
            u = priority_queue.get()[1]
            
            # For all connected nodes v to the node u with length l
            for v in E[u]:

                # Algorithm supports only positive lengths
                if l[u][v] <= 0:
                    raise ValueError('Non positive edge length (' + str(l[u][v]) + ') found.')
                    
                if distance[v] > distance[u] + l[u][v]:
                    distance[v] = distance[u] + l[u][v]
                    previous[v] = u

                    # Update priority
                    priority_queue.updatePriority(v, distance[v])

        return previous, distance
         
        
    def bfs(self, G, s):
        '''
        BFS algorithm for finding the shortest paths in a graph.
        Returns the shortest paths from node 's' to any other node together with the
        related path cost.

        Args:
            G (tuple(list,dictionary)): The graph G = (V,E).
            s (string): Starting node.
            
            Note: The edges of the graph considered as having unit length.

        Returns:
            previous (dictionary): The previous data structure of the algorithm.
            distance (dictionary): The distance data structure of the algorithm.
            
            Backtracking the previous structure we can get the shortest path from
            the starting node to any other node. Path cost is the distance[terminating_node].
        '''
        
        # Initializations
        V = G[0]
        E = G[1]
        # Initialize distances as defined in the algorithm
        distance = {key: float('inf') for key in V}
        distance[s] = 0
        
        # FIFO queue contains nodes
        Q = Queue()
        # Initialize the queue as defined in the algorithm
        Q.put(s)
        
        # Initialize the previous structure. This is for bactracking the shortest path.
        # Is not included in the original algorithm.
        previous = {}
        
        while not Q.empty():
            u = Q.get()

             # For all connected nodes v to the node u
            for v in E[u]:
                
                if distance[v] == float('inf'):
                    Q.put(v)
                    distance[v] = distance[u] + 1
                    previous[v] = u
         
        return previous, distance
        
        
    def dfs(self, G):
        '''
        DFS algorithm for revealing a wealth of information about a graph. 
        Returns information about the feasible paths among all the nodes in 
        the graph.

        Args:
            G (tuple(list,dictionary)): The graph G = (V,E).

        Returns:
            pre (dictionary): The time of the first discovery to each node.
            post (dictionary): The time of the last departure from each node.
            ccnum (dictionary): The connected component id of each node.
        '''

        # Nested functions used only by DFS
        # See DPV, Algorithms, Chapter 3.2
        def previsit(v):
            nonlocal clock
            nonlocal cc
            pre[v] = clock
            clock = clock +  1
            ccnum[v] = cc
        
        def postvisit(v):
            nonlocal clock
            post[v] = clock
            clock += 1
        
        def explore(v):
            visited[v] = True
            previsit(v)
            for u in E[v]:
                if not visited[u]:
                    explore(u)
            postvisit(v)
                    
        
        # Initializations
        V = G[0]
        E = G[1]
        
        # Time of first visit to a node
        pre = {}
        # Time of final departure from a node
        post = {}
        # Time
        clock = 1
        
        # Connected components identification
        ccnum = {}
        cc = 0

        # Visited is initialized to False for all vertices of the graph
        visited = {v: False for v in V}
        
        for v in V:
            if not visited[v]:
                cc += 1
                explore(v)
                
        return pre, post, ccnum
        
        
    def bellmanFord(self, G, l, s):
        '''
        Bellman-Ford algorithm for finding the shortest paths in a graph.
        Returns the shortest paths from node 's' to any other node together
        with the related path cost.

        Args:
            G (tuple(list,dictionary)): The graph G = (V,E).
            l (dictionary): The edges lengths of the graph G = (V,E).
            s (string): Starting node.

        Returns:
            previous (dictionary): The previous data structure of the algorithm.
            distance (dictionary): The distance data structure of the algorithm.
            
            Backtracking the previous structure we can get the shortest path from
            the starting node to any other node. Path cost is the distance[terminating_node].
        '''

        # Initializations
        V = G[0]
        E = G[1]
        # Initialize distances as defined in the algorithm
        distance = {key: float('inf') for key in V}
        distance[s] = 0
        
        # Initialize the previous structure as defined in the algorithm
        previous = {key: None for key in V}
        
        # Repeat |V| - 1 times
        for _ in range(len(V)-1):
            for u in V:
                for v in E[u]:
                    if distance[v] > distance[u] + l[u][v]:
                        distance[v] = distance[u] + l[u][v]
                        previous[v] = u
                    
        return previous, distance


class MST(object):
    '''
    Minimum Spanning Tree algorithms implementation. See methods for the implemented 
    algorithms.

    Args:
        -

    Attributes:
        -
        
    Methods:
        kruskal(self, G, w) : Implementation of the Kruskal's algorithm.
    '''

    def __init__(self):
  
        raise NotImplementedError()
        
    
    def kruskal(self, G, w):
        '''
        Kruskals algorithm for finding the Minimum Spanning Tree in a graph.
        Returns the MST and its total weight.

        Args:
            G (tuple(list,dictionary)): The graph G = (V,E).
            w (dictionary): The edges weights of the graph G = (V,E).

        Returns:
            mst (Graph): The minimum spanning tree.
            weights (dictionary): The edges weights of the minimum spanning tree.
            total_weight (float): The total weight of the minimum spanning tree.
        '''
        
        raise NotImplementedError()
    
    