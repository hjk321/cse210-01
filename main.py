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

def turn_input(boards, player):
    pass

def check_game_end(boards):
    pass

if __name__ == "__main__":
    main()
