import copy
import heapq


class Set:
    def __init__(self):
        self.thisSet = set()

    def add(self, entry):
        if entry is not None:
            self.thisSet.add(entry.__hash__())

    def length(self):
        return len(self.thisSet)

    def is_member(self, query):
        return query.__hash__() in self.thisSet


class State():
    # TODO: this might only work with the starting board rather than just any board maybe pass in x,y or find it?
    def __init__(self, tiles):
        self.xpos = 0
        self.ypos = 0
        self.tiles = tiles

    def set_x_y(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 0:
                    self.ypos = col
                    self.xpos = row

    def left(self):
        if (self.ypos == 0):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos][s.ypos - 1]
        s.ypos -= 1
        s.tiles[s.xpos][s.ypos] = 0
        return s

    def right(self):
        if (self.ypos == 2):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos][s.ypos + 1]
        s.ypos += 1
        s.tiles[s.xpos][s.ypos] = 0
        return s

    def up(self):
        if (self.xpos == 0):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos - 1][s.ypos]
        s.xpos -= 1
        s.tiles[s.xpos][s.ypos] = 0
        return s

    def down(self):
        if (self.xpos == 2):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos + 1][s.ypos]
        s.xpos += 1
        s.tiles[s.xpos][s.ypos] = 0
        return s

    def __hash__(self):
        return (tuple(self.tiles[0]), tuple(self.tiles[1]), tuple(self.tiles[2]))

    def __str__(self):
        return '%d %d %d\n%d %d %d\n%d %d %d' % (
            self.tiles[0][0], self.tiles[0][1], self.tiles[0][2],
            self.tiles[1][0], self.tiles[1][1], self.tiles[1][2],
            self.tiles[2][0], self.tiles[2][1], self.tiles[2][2])

    def copy(self):
        s = copy.deepcopy(self)
        return s

class PriorityQueue:
    def __init__(self):
        self.thisQueue = []

    def push(self, new_node):
        heapq.heappush(self.thisQueue, (new_node.cost, -new_node.id, new_node))

    def pop(self):
        return heapq.heappop(self.thisQueue)[2]

    def is_empty(self):
        return len(self.thisQueue) == 0

    def length(self):
        return len(self.thisQueue)


node_id = 0


class Node:
    def __init__(self, state, parent, heuristic):
        global node_id
        self.id = node_id
        node_id += 1
        self.parent = parent
        self.depth = parent.depth + 1 if parent is not None else 0
        self.cost = self.get_cost(heuristic)
        self.state = state

    def get_cost(self, heuristic):
        if heuristic == 0:
            return self.depth

        if heuristic == 1:
            return self.depth + self.get_displacment_cost()

        if heuristic == 2:
            return self.depth + self.get_manhattan_cost()

        if heuristic == 3:
            return self.depth + self.get_my_super_cool_cost()


    def __str__(self):
        return 'Node: id=%d Depth=%d \nstate:  \n' % (self.id, self.depth) + self.state.__str__()

    def get_manhattan_cost(self):
        return 0

    def get_displacment_cost(self):
        return 0

    def get_my_super_cool_cost(self):
        return 0


