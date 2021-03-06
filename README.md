# data-structures
Sample code for a number of classic data structures implemented in Python

## Build Status
[![Build Status](https://travis-ci.org/MigrantJ/data-structures.svg?branch=wgraph)](https://travis-ci.org/MigrantJ/data-structures) 

## linked_list
### Collaborators
- Jim Grant
- Johnson Jew


## stack
### Collaborators
- Jim Grant
- Johnson Jew

### References
http://stackoverflow.com/questions/49002/prefer-composition-over-inheritance


## queue
### Collaborators
- Jim Grant
- Johnson Jew


## dllist
### Collaborators
- Jim Grant
- Johnson Jew

### Use Cases
A doubly-linked list should be used instead of a standard linked list whenever
the data can be added or removed from either end. For example, if one were
modeling a series of lego blocks, with the desire to either put a new block on
top, or put the entire stack on top of another block. Any model that needs to
build elements "out from the middle", instead of from one end or another, is
an ideal use case.


## bst
METHODS
size():  returns number of nodes
balance():  returns positive, negative or zero value as it relates to the balance of the tree.
depth():  returns the depth of the tree as an integer
insert(value):  creates a new node of a given value and places it appropriately.
TRAVERSAL METHODS
in_order()
pre_order()
post_order()
breadth_first()
^ returns a list of nodes in the order specified.
Inspiration for depth and balance methods taken from [Jonathan Stallings](https://github.com/jonathanstallings/data-structures/blob/feature/bst/bst.py).
delete(node): removes the node in question and moves other nodes accordingly.


## insertion-sort
Iterate through the list from left to right, comparing each value to the 
previous values until it finds one that it is greater than or it reaches the 
beginning of the list.

Benefits:
- Simple to implement
- Fast at small arrays

Best Case: O(n)

Worst Case: O(n^2)

Average Case: O(n^2)

### Collaborators
- Jim Grant
- Megan Slater

### References
- [Pseudocode Algorithm](https://en.wikipedia.org/wiki/Insertion_sort)
- [Timeit Reference](https://github.com/tlake/data-structures-mk2/blob/hashtable/structures/hash_table.py)


## parenthetical.parens()
Return an integer representing whether all open parentheses are closed in order in the provided input.


## graph
### Collaborators
- Jim Grant
- Johnson Jew

### Path Algorithms
sp_dijkstra - An implementation of Dijkstra's algorithm. Iterates through all 
"unvisited" nodes, selecting the one with the lowest estimated weight each time
to find the lowest-cost route to all other nodes in the graph. Once this is 
done, it follows the chain backwards from the destination node to return the 
path.

sp_bellmanford - An implementation of the Bellman-Ford algorithm. Unlike 
Dijkstra's algorithm, Bellman-Ford does not preferentially select nodes while 
calculating weights. This makes it take longer, but allows it to process graphs
which have negatively-weighted edges.


## hash-table
### Collaborators
- Jim Grant
- Megan Slater
The hash table hashes and stores keys and their values for quick retreival.
Methods include:

get(key): returns the value stored with the given key
set(key, val): stores the given val using the given key
hash(key): hashes the key provided
