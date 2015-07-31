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

## hash-table
###Collaborators
- Jim Grant
- Megan Slater

The hash table hashes and stores keys and their values for quick retreival.
Methods include:

get(key): returns the value stored with the given key
set(key, val): stores the given val using the given key
hash(key): hashes the key provided
