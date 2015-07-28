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

## bst
###Collaborators
- Jim Grant
- Megan Slater

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


###Use Cases
A doubly-linked list should be used instead of a standard linked list whenever
the data can be added or removed from either end. For example, if one were
modeling a series of lego blocks, with the desire to either put a new block on 
top, or put the entire stack on top of another block. Any model that needs to 
build elements "out from the middle", instead of from one end or another, is
an ideal use case.
