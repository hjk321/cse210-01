# Supplementary printing vars/functions

import sys

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
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY  = "\033[1;30m"
RESET      = "\033[0;0m"

def print_color(color, message, end="\n"):
    sys.stdout.write(color)
    print(message, end=end)
    sys.stdout.write(RESET)

def print_boards():
    pass

def print_board_space(board, space):
    pass

def print_player_icon(player):
    pass
