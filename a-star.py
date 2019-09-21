import sys
from Search import PriorityQueue, Node, Set, State

if len(sys.argv) != 2:
    print(
        "Please enter a heuristic: 0 - No Heuristic, 1 - Tile Displacement, 2 - Manhattan Distances, 3 - My super "
        "terrible heuristic")
    sys.exit(0)

goal_state = State([[0, 1, 2], [3, 4, 5], [6, 7, 8]])


def main():
    heuristic = int(sys.argv[1])
    frontier = PriorityQueue()
    closed = Set()
    frontier.push(get_start_node(heuristic))
    search(frontier, closed, heuristic)


def get_start_node(heuristic):
    # board = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]

    board = [[int(n) for n in line.split()] for line in sys.stdin]
    start_node = Node(State(board), None, heuristic)
    start_node.state.set_x_y(board)
    return start_node


def search(frontier, closed, heuristic):
    goal_is_found = False
    while not frontier.is_empty():

        current_node = frontier.pop()

        # add to closed list
        closed.add(current_node.state)

        # generate children
        frontier = successors(current_node, frontier, closed, heuristic)

        # goal check
        goal_is_found = current_node.state.__hash__() == goal_state.__hash__()
        if goal_is_found:
            print_stats(current_node, frontier, closed)
            break

    if not goal_is_found:
        print("Didnt find goal")


def successors(parent, frontier, closed, heuristic):
    up = parent.state.up()
    if up is not None and not closed.is_member(up):
        frontier.push(Node(up, parent, heuristic))

    down = parent.state.down()
    if down is not None and not closed.is_member(down):
        frontier.push(Node(down, parent, heuristic))

    left = parent.state.left()
    if left is not None and not closed.is_member(left):
        frontier.push(Node(left, parent, heuristic))

    right = parent.state.right()
    if right is not None and not closed.is_member(right):
        frontier.push(Node(right, parent, heuristic))

    return frontier


def print_stats(current_node, frontier, closed):
    print("V=", closed.length())
    print("N=", closed.length() + frontier.length())
    print("d=", current_node.depth)
    print("b=", pow(closed.length() + frontier.length(), (1 / current_node.depth)), '\n')

    stack = []
    while current_node.parent is not None:
        stack.append(current_node.state)
        current_node = current_node.parent

    stack.append(current_node.state)

    while len(stack) != 0:
        print(stack.pop(), '\n')


if __name__ == '__main__':
    main()
