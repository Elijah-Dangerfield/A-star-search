import sys, random
import Search
if len(sys.argv) != 3:
    print()
    print("Usage: %s [seed] [number of random moves]" % (sys.argv[0]))
    print()
    sys.exit(1)


def main():
    board = [[int(n) for n in line.split()] for line in sys.stdin]
    state = Search.State(board)
    random.seed(int(sys.argv[1]))
    number_of_moves = int(sys.argv[2])

    for i in range(number_of_moves):
        move = random.randrange(4)
        state = move_board(state, move)
        print(state)


def move_board(state, move):
    original = state

    if move == 0:
        print("UP")
        state = state.up()
        return state if state is not None else original

    elif move == 1:
        print("DOWN")

        state = state.down()
        return state if state is not None else original

    elif move == 2:
        print("LEFT")

        state = state.left()
        return state if state is not None else original

    else:
        print("RIGHT")

        state = state.right()
        return state if state is not None else original


if __name__ == '__main__':
    main()
