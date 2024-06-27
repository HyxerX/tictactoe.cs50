"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if len(actions(board)) % 2 == 1:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i = 0
    j = 0

    possible_actions = set()

    for row in board:
        for cell in row:
            if cell == None:
                res = (i, j)
                possible_actions.add(res)
            j += 1
        j = 0
        i += 1

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    valid_action = False

    new_board = deepcopy(board)
    i, j = action

    for _action in actions(board):
        if action == _action:
            valid_action = True

    if not valid_action:
        raise Exception

    new_board[i][j] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    value = utility(board)

    if value == 1:
        return X
    elif value == -1:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) == 0 or utility(board) != 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            if board[i][0] == X:
                return 1
            elif board[i][0] == O:
                return -1

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            if board[0][i] == X:
                return 1
            elif board[0][i] == O:
                return -1

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        if board[0][0] == X:
            return 1
        elif board[0][0] == O:
            return -1

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        if board[0][2] == X:
            return 1
        elif board[0][2] == O:
            return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -5
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                if minval > v:
                    v = minval
                    optimal_move = action
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 5
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    optimal_move = action
            return v, optimal_move

    curr_player = player(board)
    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]


# print(minimax(initial_state()))

# print(result(initial_state(), (0, 1)))

# print(terminal(initial_state()))

# print(utility(initial_state()))

# print(player(initial_state()))

# print(actions(initial_state()))
