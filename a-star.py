import sys
import random
import Search
import heapq

# we will need some static variable to increment for previous assigned id a
# frontier ties will be broken by higher ID
# we would need to travel back to parent via pointers and add to a stack to pop off for printing result



# create a function to create a starting state given the input
# that function will need to populate some class with the info, might be reused

# create function given node to compute f(n) using the heuristic passed in

# create an expand function that checks goal, adds to closed list, and generates children (can use random_board move) and returns
#boolean for goal check

#create serch function that while (goal not exapnded) expands the current node and sets the boolean for the while


# TODO: using pointers and tracking paths and using closed and open list and poping back to answer needs to be done

if len(sys.argv) != 2:
    print()
    print("Usage: %s [heuristic]" % (sys.argv[0]))
    print()
    sys.exit(1)


def main():
    frontier = Search.PriorityQueue
    closed = Search.Set()

    board = [[int(n) for n in line.split()] for line in sys.stdin]
    start_node = Search.Node(board)


if __name__ == '__main__':
    main()
