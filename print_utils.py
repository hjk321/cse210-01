# Supplementary printing vars/functions

import sys
from global_defs import *

#  0 | 1 | 2  #
# ----------  #
#  3 | 4 | 5  #
# ----------  #
#  6 | 7 | 8  #

space_chars = [
    ["1","2","3","4","5","6","7","8","9"],
    ["A","B","C","D","E","F","G","H","I"],
    ["a","b","c","d","e","f","g","h","i"]]

# ANSI codes courtesy of rene-d on Github
# https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
RED        = "\033[1;31m"  
BLUE       = "\033[1;34m"
GREEN      = "\033[1;32m"
CYAN       = "\033[1;36m"
YELLOW     = "\033[1;33m"
PURPLE     = "\033[0;35m"
LIGHT_GRAY = "\033[2m\033[0;37m"
DARK_GRAY  = "\033[2m\033[1;30m"
RESET      = "\033[0;0m"

# Print text with color.
def print_color(color, message, end="\n"):
    sys.stdout.write(color)
    print(message, end=end)
    sys.stdout.write(RESET)

# Prints all three boards for viewing by the player.
def print_boards(boards):
    def print_board_row(spaces):
        print(" ", end="")
        print_board_space(boards, *spaces[0])
        print(" | ", end="")
        print_board_space(boards, *spaces[1])
        print(" | ", end="")
        print_board_space(boards, *spaces[2])
        print("       ", end="")
        print_board_space(boards, *spaces[3])
        print(" | ", end="")
        print_board_space(boards, *spaces[4])
        print(" | ", end="")
        print_board_space(boards, *spaces[5])
        print("       ", end="")
        print_board_space(boards, *spaces[6])
        print(" | ", end="")
        print_board_space(boards, *spaces[7])
        print(" | ", end="")
        print_board_space(boards, *spaces[8])
        print()

    # Pass board/space pairs for each row.
    print_board_row([[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]])
    print(" ---------------       ---------------       ---------------")
    print_board_row([[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]])
    print(" ---------------       ---------------       ---------------")
    print_board_row([[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]])

# Prints a board space. If the space is occupied, prints a player icon.
# If the space is empty, it will print the input char corresponding to that space.
def print_board_space(boards, board, space):
    val = boards[board][space]
    print(" ", end="")
    if val != NONE:
        print_player_icon(val)
    else:
        char = space_chars[board][space]
        print_color(LIGHT_GRAY, char, end="")
    print(" ", end="")
    
# Prints a colored icon representing a player.
def print_player_icon(player):
    if player == PLAYER_X:
        print_color(BLUE, "X", end="")
    elif player == PLAYER_O:
        print_color(RED, "O", end="")
    elif player == PLAYER_A:
        print_color(GREEN, "&", end="")
    else:
        print(" ", end="")
