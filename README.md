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
1. *Introduction to Algorithms, 3rd Edition. T. H. Cormen, C. E. Leiserson, R. L. Rivest, C. Stein. Chapter VI, Graph Algorithms*
2. *Algorithms. S. Dasgupta, C. Papadimitriou, U. Vazirani. Chapter 3, Decompositions of Graphs*
3. *Algorithms. S. Dasgupta, C. Papadimitriou, U. Vazirani. Chapter 4, Paths in Graphs*
4. *Algorithms. S. Dasgupta, C. Papadimitriou, U. Vazirani. Chapter 5, Greedy Algorithms*
5. *Algorith Design, 1st Edition. J. Kleinberg, E. Tardos. Chapter 3, Graphs*

