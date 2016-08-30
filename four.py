# Possible game states
WIN = "W"
LOSE = "L"
TIE = "T"
UNDECIDED = "U"

# Starting number
N = 4

"""
Checks what state the given position is in: W, L, T, U
To clarify, it's given that you're presented with this position, have you
won, loss, tied, or is it undecided?
"""
def primitive(pos):
    if pos == 0:
        return LOSE
    else:
        return UNDECIDED

"""
Returns the starting position of the game.
"""
def initial_position():
    return N

"""
Performs a move on a position, returning the resulting position.
"""
def do_moves(move, pos):
    return pos - move

"""
Returns a list of all possible moves that can be made
"""
def gen_moves(pos):
    if pos > 1:
        return [1, 2]
    elif pos > 0:
        return [1]
    else:
        return []