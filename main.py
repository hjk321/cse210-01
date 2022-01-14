# CSE210 Tic-Tac-Toe Assignment.
# Written by Hiram Anderson

from print_utils import *

# Multipurpose ID vars. Used for data storage, win checking, etc.
NONE = 0
PLAYER_X = 1
PLAYER_O = 2
PLAYER_A = 3
TIE = 4

# Main function.
def main():
    title_screen()

    # Init game vars
    turn = -1
    boards = [[NONE] * 9] * 3

    # Keep doing turns until the game ends.
    while True:
        print("\n-------------------------------")
        print_boards()
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
    print_color(CYAN, "Three Players.")
    print()
    input("Press enter to start... ")

def turn_input(boards, player):
    pass

def check_game_end(boards):
    pass

if __name__ == "__main__":
    main()
