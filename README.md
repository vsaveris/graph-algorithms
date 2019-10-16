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

## Prerequisites
1. [python 3.6](https://www.python.org/downloads/release/python-369/)

## References
1. *Introduction to Algorithms, 3rd Edition, Chapter VI, Graph algorithms*
2. *DPV Algorithms, Chapter 3, Decompositions of graphs*
3. *DPV Algorithms, Chapter 4.4, Paths in graphs*

