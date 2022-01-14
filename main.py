# CSE210 Tic-Tac-Toe Assignment.
# Written by Hiram Anderson

from global_defs import *
from print_utils import *

# Main function.
def main():
    title_screen()

    # Init game vars
    turn = -1
    boards = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

    # Keep doing turns until the game ends.
    while True:
        print()
        print_boards(boards)
        print()
        turn += 1
        player = (turn % 3) + 1
        turn_input(boards, player)
        if check_game_end(boards) != NONE:
            break;
    
    # The game has ended
    print("The game has ended. Placeholder message.")

# Prints the title screen and waits for enter press.
def title_screen():
    print_color(BLUE, "Tic", end="")
    print("-", end="")
    print_color(RED, "Tac", end="")
    print("-", end="")
    print_color(GREEN, "Tri")
    print_color(PURPLE, "Three Boards. ", end="")
    print_color(CYAN, "Three Players. ", end="")
    print_color(YELLOW, "One Winner.")
    print()
    input("Press enter to start... ")

# Handles and validates input of a player making a move on the board.
def turn_input(boards, player):
    def get_space_from_char(char):
        for b in range(0, 3):
            for s in range(0, 9):
                if char == space_chars[b][s]:
                    return (b, s)
        return (None, None)

    # Loop until valid input
    while True:
        print_player_icon(player)
        char = input("\'s turn. Enter a space (1-9, A-I, a-i): ")
        if len(char) == 0:
            continue
        char = char[0]
        board, space = get_space_from_char(char)
        if board == None:
            print("Invalid character.")
            continue
        # Check if space is empty, and if so, assign this player to that space.
        if boards[board][space] == NONE:
            boards[board][space] = player
            break
        print("Space already taken.")

def check_game_end(boards):
    def check_spaces(board, a, b, c):
        if board[a] == board[b] == board[c]:
            return board[a]
        return NONE

    # We'll check each board independently since they all have the same rules.
    # If a win is found on a board, the function early-exits out.
    for board in boards:
        val = check_spaces(board, 0, 1, 2)
        if val != NONE: return val
        val = check_spaces(board, 3, 4, 5)
        if val != NONE: return val
        val = check_spaces(board, 6, 7, 8)
        if val != NONE: return val
        val = check_spaces(board, 0, 3, 6)
        if val != NONE: return val
        val = check_spaces(board, 1, 4, 7)
        if val != NONE: return val
        val = check_spaces(board, 2, 5, 8)
        if val != NONE: return val
        val = check_spaces(board, 0, 4, 8)
        if val != NONE: return val
        val = check_spaces(board, 6, 4, 2)
        if val != NONE: return val

    # No win found. We now need to check for empty spaces, and declare a draw if not.
    for board in boards:
        for space in board:
            if space == NONE: return NONE
    return DRAW

if __name__ == "__main__":
    main()
