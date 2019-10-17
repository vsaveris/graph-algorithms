# graph-algorithms
## Description
Implementation of graph algorithms in python (file: `graphalgorithms.py`)
* **Depth-first search (DFS)**: DFS algorithm is an algorithm for revealing a wealth of information about a graph G = (V,E). The time complexity of the algorithm is O(|V|+|E|).
* **Breadth-first search (BFS)**: BFS algorithm is an algorithm for finding the shortest paths in any graph G = (V,E) whose edges have unit length. The time complexity of the algorithm is O(|V|+|E|).
* **Dijkstra's Algorithm**: Dijkstra's algorithm is an algorithm for finding the shortest paths in any graph G = (V,E) whose edges lengths are positive numbers. The time complexity of the algorithm is O((|V|+|E|)log|V|), when using a priority queue.

## Demonstration
Inside the `demo` folder there is a demonstration script (`demoga.py`), including usage examples for the `GraphAlgorithms` class.
```
$python demoga.py -h
usage: demoga.py [-h] -a algorithm

Demonstration script for the GraphAlgorithms class

optional arguments:
  -h, --help    show this help message and exit
  -a algorithm  demonstration algorithm

Supported values for 'algorithm' are ('dfs', 'bfs','dijkstra')

Example:
python demoga.py -a dijkstra
```
The graphs used in each algorithm case for the demonstration purposes are shown below.

### DFS Demonstration Graph
![](/images/dfs_demo_graph.PNG?raw=true)

In the running example, the DFS algorithm reveals all the connected components of the given graph together with the first discovery and last departure times for each node. The output of the algorithm is:
```
$python demoga.py -a dfs
DFS output for the given graph:
node 'A': first_discovery_time =  1,last_departure_time = 10, connected_component =  1
node 'B': first_discovery_time =  2,last_departure_time =  3, connected_component =  1
node 'C': first_discovery_time = 11,last_departure_time = 22, connected_component =  2
node 'D': first_discovery_time = 12,last_departure_time = 21, connected_component =  2
node 'E': first_discovery_time =  4,last_departure_time =  9, connected_component =  1
node 'F': first_discovery_time = 23,last_departure_time = 24, connected_component =  3
node 'G': first_discovery_time = 16,last_departure_time = 19, connected_component =  2
node 'H': first_discovery_time = 13,last_departure_time = 20, connected_component =  2
node 'I': first_discovery_time =  5,last_departure_time =  8, connected_component =  1
node 'J': first_discovery_time =  6,last_departure_time =  7, connected_component =  1
node 'K': first_discovery_time = 17,last_departure_time = 18, connected_component =  2
node 'L': first_discovery_time = 14,last_departure_time = 15, connected_component =  2
connected component 1: ['A', 'B', 'E', 'I', 'J']
connected component 2: ['C', 'D', 'H', 'L', 'G', 'K']
connected component 3: ['F']
``` 

### BFS Demonstration Graph
![](/images/bfs_demo_graph.PNG?raw=true)

In the running example, the BFS algorithm calculates all the shortest paths from the starting node `B`. The output of the algorithm is:
```
$python demoga.py -a bfs
BFS shortest paths for the given graph, where starting node is 'B':
Shortest path from 'B' to 'A' is: ['B', 'A'] with cost 1
Shortest path from 'B' to 'C' is: ['B', 'C'] with cost 1
Shortest path from 'B' to 'D' is: ['B', 'A', 'S', 'D'] with cost 3
Shortest path from 'B' to 'E' is: ['B', 'A', 'S', 'E'] with cost 3
Shortest path from 'B' to 'S' is: ['B', 'A', 'S'] with cost 2
``` 

### Dijkstra Demonstration Graph
![](/images/dijkstra_demo_graph.PNG?raw=true)

In the running example, the Dijkstra's algorithm calculates all the shortest paths from the starting node `A`. The output of the algorithm is:
```
$python demoga.py -a dijkstra
Dijkstra shortest paths for the given graph, where starting node is 'A':
Shortest path from 'A' to 'B' is: ['A', 'C', 'B'] with cost 3
Shortest path from 'A' to 'C' is: ['A', 'C'] with cost 2
Shortest path from 'A' to 'D' is: ['A', 'C', 'B', 'D'] with cost 6
Shortest path from 'A' to 'E' is: ['A', 'C', 'B', 'E'] with cost 7
``` 

## Prerequisites
1. [python 3.6](https://www.python.org/downloads/release/python-369/)

## References
1. *Introduction to Algorithms, 3rd Edition. T. H. Cormen, C. E. Leiserson, R. L. Rivest, C. Stein. Chapter VI, Graph Algorithms*
2. *Algorithms. S. Dasgupta, C. Papadimitriou, U. Vazirani. Chapter 3, Decompositions of Graphs*
3. *Algorithms. S. Dasgupta, C. Papadimitriou, U. Vazirani. Chapter 4, Paths in Graphs*
4. *Algorithms. S. Dasgupta, C. Papadimitriou, U. Vazirani. Chapter 5, Greedy Algorithms*
5. *Algorith Design, 1st Edition. J. Kleinberg, E. Tardos. Chapter 3, Graphs*

