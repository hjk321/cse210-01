from print_utils import *

def main():
    print_color(BLUE, "Tic", end="")
    print("-", end="")
    print_color(RED, "Tac", end="")
    print("-", end="")
    print_color(GREEN, "Tri")
    print_color(PURPLE, "Three Boards. ", end="")
    print_color(CYAN, "Three Players.")
    print()
    input("Press enter to start... ")

if __name__ == "__main__":
    main()
