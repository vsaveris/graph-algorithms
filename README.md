# graph-algorithms
## Description
Implementation of graph algorithms in python (file: `graphalgorithms.py`)
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

Supported values for 'algorithm' are ('bfs','dijkstra')

Example:
python demoga.py -a dijkstra
```
The graphs used in each algorithm case for the demonstration purposes are shown below.

### BFS Demonstration Graph
![](/images/dfs_demo_graph.PNG?raw=true)

In the running example, the BFS algorithm calculates all the shortest paths from the starting node `B`. The output of the algorith is:
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

In the running example, the Dijkstra's algorithm calculates all the shortest paths from the starting node `A`. The output of the algorith is:
```
PUT output
``` 

## Prerequisites
1. [python 3.6](https://www.python.org/downloads/release/python-369/)

## References
1. *Introduction to Algorithms, 3rd Edition. T. H. Cormen, C. E. Leiserson, R. L. Rivest, C. Stein. Chapter VI, Graph Algorithms*
2. *Algorithms. S. Dasgupta, C. Papadimitriou, U. Vazirani. Chapter 3, Decompositions of Graphs*
3. *Algorithms. S. Dasgupta, C. Papadimitriou, U. Vazirani. Chapter 4, Paths in Graphs*
4. *Algorithms. S. Dasgupta, C. Papadimitriou, U. Vazirani. Chapter 5, Greedy Algorithms*
5. *Algorith Design, 1st Edition. J. Kleinberg, E. Tardos. Chapter 3, Graphs*

