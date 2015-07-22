# data-structures
Sample code for a number of classic data structures implemented in Python

## Build Status
[![Build Status](https://travis-ci.org/MigrantJ/data-structures.svg?branch=wgraph)](https://travis-ci.org/MigrantJ/data-structures) 

##linked_list
###Collaborators
- Jim Grant
- Johnson Jew


## stack
###Collaborators
- Jim Grant
- Johnson Jew

###References
http://stackoverflow.com/questions/49002/prefer-composition-over-inheritance


## queue
###Collaborators
- Jim Grant
- Johnson Jew


## dllist
###Collaborators
- Jim Grant
- Johnson Jew

###Use Cases
A doubly-linked list should be used instead of a standard linked list whenever
the data can be added or removed from either end. For example, if one were
modeling a series of lego blocks, with the desire to either put a new block on 
top, or put the entire stack on top of another block. Any model that needs to 
build elements "out from the middle", instead of from one end or another, is
an ideal use case.

## graph
###Collaborators
- Jim Grant
- Johnson Jew

###Path Algorithms
sp_dijkstra - An implementation of Dijkstra's algorithm. Iterates through all 
"unvisited" nodes, selecting the one with the lowest estimated weight each time
to find the lowest-cost route to all other nodes in the graph. Once this is 
done, it follows the chain backwards from the destination node to return the 
path.

sp_bellmanford - An implementation of the Bellman-Ford algorithm. Unlike 
Dijkstra's algorithm, Bellman-Ford does not preferentially select nodes while 
calculating weights. This makes it take longer, but allows it to process graphs
which have negatively-weighted edges.
