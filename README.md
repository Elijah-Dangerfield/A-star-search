# OLA1
This is an open lab assignment for CSCI 4350, an introduction to artificail intelligence. 

The goal of this code is to test differing heuristic choices in an a-star search of finding the goal state for the famous 8 puzzle problem. 

![](http://www.aiai.ed.ac.uk/~gwickler/images/8-puzzle-states.png)

## Code

### /search 
contains all code relevent to the search. 
search.py includes all data structures used in the search. 
random_board.py returns a shuffled board for a-star.py to solve
a-star.py implements the search and prints V- the number of nodes visited N- the number of nodes in memory b- the effective branching factor and d, the depth of the solution found. 

### /results
contains all files relevant to the results of the searches. statistics.txt compiles all information for each heuristic 

h0 = no heuristic
h1 = # displaced tiles
h2 = manhattan distance
h3 = # of correct rows


