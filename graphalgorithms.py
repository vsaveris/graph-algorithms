from queue import PriorityQueue

class Graph(object):
    '''
    Graph G = (V, E) object, where V vertices and E edges.

    Args:
        vertices (list)   : A list containing the nodes of the graph.
                            i.e. ['a', 'b', 'c', 'd']
                            
        edges (dictionary): A dictionary containing the edges of the graph with
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
        __vertices (list)   : Where vertices are stored.
        __edges (dictionary): Where edges are stored.
        
    Methods:
        getVertices() : Returns the value of __vertices (list)
        getEdges()    : Returns the value of __edges (dictionary)
    '''
    
    def __init__(self, vertices, edges):
        
        self.__vertices = vertices
        self.__edges = edges
        
        # If a vertex is missing from the edges dictionary then add it with none connected nodes.
        for v in self.__vertices:
            try:
                self.__edges[v]
            except:
                self.__edges[v] = []
        
        
    
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
            edges (dictionary): The graph edges with their lengths.
            See class docstring for the dictionary details.
        '''
    
        return self.__edges
        
        

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
        dijkstra(self, g, s) : Implementation of the Dijkstra's algorithm.
    '''

    def __init__(self):
  
        pass
        
        
    def dijkstra(self, g, s):
        '''
        Dijkstra's algorithm for finding the shortest paths in a graph.
        Returns the shortest paths from node 's' to any other node and the
        related path cost.

        Args:
            g (Graph object): The graph G = (V,E).
            s (string): Starting node.
            
            Note: In the original algorithm, the lengths of the edges are
                  passed as a parameter (l), in this implementation the lengths
                  are passed with the Graph object (g.getEdges()).

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
        # Initialize distances as defined in the algorithm
        distance = {key: float('inf') for key in g.getVertices()}
        distance[s] = 0
        
        # Initialize the previous structure as defined in the algorithm
        previous = {key: None for key in g.getVertices()}
        
        # Updatable priority queue contains items of the type (priority, node)
        priority_queue = UpdatablePriorityQueue()
        # Initialize the queue as defined in the algorithm
        for v in g.getVertices():
            priority_queue.put((distance[v], v))
        
        # Loop until all the nodes are explored
        while not priority_queue.empty():
            u = priority_queue.get()[1]
            
            # For all connected nodes v to the node u with length l
            for v, l in g.getEdges()[u]:
                # Algorithm supports only positive lengths
                if l <= 0:
                    raise ValueError('Non positive edge length (' + str(l) + ') found.')
                    
                if distance[v] > distance[u] + l:
                    distance[v] = distance[u] + l
                    previous[v] = u
                    
                    # Update priority
                    priority_queue.updatePriority(distance[v], v)
                    
        return previous, distance
        
        
'''
Usage example code
'''
if __name__ == '__main__':

    '''
    Example code for Dijkstra's algorithm.
    '''
    # Define the vertices and edges of the graph, in the structure 
    # the class Graph expects them
    V = ['a', 'b', 'c', 'd', 'e', 'f', 's', 't']   
    E = {'s': [('a', 100), ('c', 90), ('e', 101)], 
         'a': [('b', 100)],
         'b': [('t', 5)],
         'c': [('d', 105)],
         'd': [('t', 10)],
         'e': [('f', 101)],
         'f': [('t', 1)]}
    
    # Create the graph object G = (V, E) given the V and E
    g = Graph(V, E)
    
    # Run Dijkstra's algorithm for the defined graph
    paths, cost = GraphAlgorithms().dijkstra(g = g, s = 's')
    
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
    
    print('Shortest path from \'s\' to \'t\' is: ', shortest_path, ' with cost ', cost['t'], sep = '')