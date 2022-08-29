"""
Tic Tac Toe Player
"""

import math

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

    number_X = 0
    number_O = 0
    # Calculate number of X and O on the board to check the turn of player
    for row in board:
        for cell in row:
            if cell == X:
                number_X += 1
            if cell == O:
                number_O += 1
    # if Xs on board are less or equal to Os then its X's turn
    if number_X <= number_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allowed_steps = set()
    # Check which cells are empty. that can be filled
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                allowed_steps.add((i, j))

    return allowed_steps


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # if game over then no result
    if action not in actions(board):
        raise Exception
    # Otherwise calculate new board
    else:
        from copy import deepcopy
        output_board = deepcopy(board)
        output_board[action[0]][action[1]] = player(board)

    return output_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check if any row is X or Y completely
    for row in board:
        if row == [X, X, X]:
            return X
        elif row == [O, O, O]:
            return O
    # Check if any column is X or Y Completely
    for i in range(3):
        column = [board[x][i] for x in range(3)]
        if column == [X, X, X]:
            return X
        if column == [O, O, O]:
            return O
    # Check if any diagonal is completely X
    if ([board[0][0], board[1][1], board[2][2]] == [X, X, X]) or ([board[0][2], board[1][1], board[2][0]] == [X, X, X]):
        return X
    # Check if any diagonal is completely O
    elif ([board[0][0], board[1][1], board[2][2]] == [O, O, O]) or ([board[0][2], board[1][1], board[2][0]] == [O, O, O]):
        return O
    # Otherwire no one won
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If anyone Won the game then over
    if winner(board) != None:
        return True

    # If any cell left empty then not over
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winn = winner(board)

    if winn == X:
        return 1
    elif winn == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    # check the current player
    current_player = player(board)

    # If empty board then provide any cell like 0,0
    if board == initial_state():
        return (0, 0)
    # minval function

    def maxValue(board):
        if terminal(board):
            return utility(board)
        v = float("-inf")
        for a in actions(board):
            res = result(board, a)
            minv = minValue(res)
            v = max(v, minv)
        return v
    # maxval function

    def minValue(board):
        if terminal(board):
            return utility(board)
        v = float("inf")
        for a in actions(board):
            res = result(board, a)
            maxv = maxValue(res)
            v = min(v, maxv)
        return v
    # IF cirrent player is X then find min
    if current_player == X:
        v = float("-inf")
        choosen_action = None
        for a in actions(board):
            minVal = minValue(result(board, a))
            if minVal > v:
                v = minVal
                choosen_action = a
    # If current player is O then find max
    elif current_player == O:
        v = float("inf")
        choosen_action = None
        for a in actions(board):
            maxVal = maxValue(result(board, a))
            if maxVal < v:
                v = maxVal
                choosen_action = a
    # return the action choosed
    return choosen_action
