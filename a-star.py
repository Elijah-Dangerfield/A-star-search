import sys
from Search import PriorityQueue, Node, Set, State

#if len(sys.argv) != 2:
   #print()
   # print()
   # sys.exit(1)


def main():
    goal_state = State([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    frontier = PriorityQueue()
    closed = Set()

    frontier.push(get_start_node())

    search(goal_state, frontier, closed)


def search(goal_state, frontier, closed):
    goal_is_found = False
    while not frontier.is_empty():

        current_node = frontier.pop()
        print("_______________CURRENT NODE ___________________\n",current_node.state)

        # add to closed list
        closed.add(current_node.state)

        # generate children
        frontier = successors(current_node, frontier, closed)



        #check if goal
        print(current_node.id)
        goal_is_found = current_node.state.__hash__() == goal_state.__hash__()
        if goal_is_found:
            print_path(current_node)
            break
    if not goal_is_found:
        print("Didnt find goal")




def print_path(current_node):
    print("Goal found with path:")

    stack = []
    while(current_node.parent != None):
        stack.append(current_node.state)
        current_node = current_node.parent

    stack.append(current_node.state)

    while len(stack) != 0:
        print(stack.pop(), '\n')






def get_start_node():
    #board = [[1, 4, 2], [3, 0, 5], [6, 7, 8]]

    board = [[int(n) for n in line.split()] for line in sys.stdin]
    start_node = Node(State(board), None)
    start_node.state.set_x_y(board)
    return start_node


def successors(parent, frontier, closed):

    up = parent.state.up()
    if up is not None and not closed.is_member(up):
        frontier.push(Node(up, parent))

    down = parent.state.down()
    if down is not None and not closed.is_member(down):
        frontier.push(Node(down, parent))

    left = parent.state.left()
    if left is not None and not closed.is_member(left):
        frontier.push(Node(left, parent))

    right = parent.state.right()
    if right is not None and not closed.is_member(right):
        frontier.push(Node(right, parent))

    return frontier


if __name__ == '__main__':
    main()
