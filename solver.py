import four

# Opposites
opposite = {four.WIN : four.LOSE, four.LOSE : four.WIN, four.TIE : four.TIE}

"""
Given a position and whose turn it is, determine whether or not the current player wins/loses
    turn: is it P1's turn
"""
def traverse_game_tree(pos):
    if four.primitive(pos) != four.UNDECIDED:
        return four.primitive(pos)
    ans = four.LOSE
    for move in four.gen_moves(pos):
        new_pos = four.do_moves(move, pos)
        result = traverse_game_tree(new_pos)
        if result == four.LOSE: # that means the opponent lost after I made this move
            ans = four.WIN
    return ans

init_pos = four.initial_position()
ans = traverse_game_tree(init_pos)
if ans == four.WIN:
    print("Player 1 wins.")
elif ans == four.LOSE:
    print("Player 2 wins.")
else:
    print("What? How did this happen?")
