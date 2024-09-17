# Tic Tac Toe game in Python

board = [' ' for _ in range(9)] # Initialize the game board

def print_board():
    """Print the current state of the game board"""
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def check_win():
    """Check if there is a winner"""
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Tie'
    return False

import random


def game():
    """Main game loop"""
    current_player = 'X'
    while True:
        print_board()
        if current_player == 'X':
            while True:
                try:
                    move = input("Player {}, enter your move (1-9): ".format(current_player))
                    move = int(move)
                    if move < 1 or move > 9:
                        print("Invalid move, please enter a number between 1 and 9.")
                        continue
                    if board[move - 1] != ' ':
                        print("Invalid move, space already occupied. Try again.")
                        continue
                    board[move - 1] = current_player
                    break
                except ValueError:
                    print("Invalid input, please enter a number.")
        else:
            # Bot's turn
            available_moves = [i for i, x in enumerate(board) if x == ' ']
            if not available_moves:
                print("No more moves left, it's a tie!")
                break
            move = random.choice(available_moves) + 1
            print("Bot's move: {}".format(move))
            board[move - 1] = current_player

        result = check_win()
        if result:
            print_board()
            if result == 'Tie':
                print("It's a tie!")
            else:
                print("Player {} wins!".format(result))
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    game()