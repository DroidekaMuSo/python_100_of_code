import random

cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

game_is_on = True


def print_board():
    print(f"""
    {cells[0]}|{cells[1]}|{cells[2]}
    {cells[3]}|{cells[4]}|{cells[5]}
    {cells[6]}|{cells[7]}|{cells[8]}
""")


def is_valid_move(position):
    return 0 <= position < 9 and cells[position] not in ["X", "O"]


def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for condition in win_conditions:
        if cells[condition[0]] == cells[condition[1]] == cells[condition[2]] and cells[condition[0]] in ["X", "O"]:
            return cells[condition[0]]

    return None


def tic_tac_toe():
    game_is_on = True

    while game_is_on:
        print_board()

        while True:
            try:
                player = int(input("Which position do you want to allocate your X (1-9)? ")) - 1
                if is_valid_move(player):
                    break
                else:
                    print("Cell already selected or out of range, choose another one")
            except (ValueError, IndexError):
                print("Invalid input, please enter a number between 1 and 9")

        cells[player] = "X"

        if check_winner():
            print_board()
            print("Player wins!")
            break

        if all(cell in ["X", "O"] for cell in cells):
            print_board()
            print("It's a tie!")
            break

        # Computer's turn
        while True:
            computer = random.randint(0, 8)
            if is_valid_move(computer):
                break

        cells[computer] = "O"

        if check_winner():
            print_board()
            print("Computer wins!")
            break

        if all(cell in ["X", "O"] for cell in cells):
            print_board()
            print("It's a tie!")
            break


tic_tac_toe()
