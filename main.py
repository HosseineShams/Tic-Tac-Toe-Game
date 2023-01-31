#Hossein SHams Esfand Abadi Student ID: 4003333008 - Final Project
from random import choice
from math import inf
from colorama import Fore, Style

#player constants
x_player = +1
o_player = -1
EMPTY = 0

#create empty game board
board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

#function to print current game board
green_down_angle = '\u2514'
green_down_right = '\u2518'
green_right_up = '\u2510'
green_up_left = '\u250C'
green_middle_junction = '\u253C'
green_top_junction = '\u252C'
green_bottom_junction = '\u2534'
green_right_junction = '\u2524'
green_left_junction = '\u251C'
green_bar = Style.BRIGHT + Fore.GREEN + '\u2502' + Fore.RESET + Style.RESET_ALL
green_dash = '\u2500'
green_first_line = Style.BRIGHT + Fore.GREEN + green_up_left + green_dash + green_dash + green_dash + green_top_junction + green_dash + green_dash + green_dash + green_top_junction + green_dash + green_dash + green_dash + green_right_up + Fore.RESET + Style.RESET_ALL
green_middle_line = Style.BRIGHT + Fore.GREEN + green_left_junction + green_dash + green_dash + green_dash + green_middle_junction + green_dash + green_dash + green_dash + green_middle_junction + green_dash + green_dash + green_dash + green_right_junction + Fore.RESET + Style.RESET_ALL
green_last_line = Style.BRIGHT + Fore.GREEN + green_down_angle + green_dash + green_dash + green_dash + green_bottom_junction + green_dash + green_dash + green_dash + green_bottom_junction + green_dash + green_dash + green_dash + green_down_right + Fore.RESET + Style.RESET_ALL

def print_board(array):
    print(green_first_line)
    for a in range(len(array)):
        for i in array[a]:
            if i == EMPTY:
                print(green_bar, ' ', end = ' ')
            else:
                if i == 1:
                    print(green_bar, "X", end = ' ')
                else:
                    print(green_bar, "O", end = ' ')
        print(green_bar)
        if a == 2:
            print(green_last_line)
        else:
            print(green_middle_line)

#function to clear game board
def clear_Board(brd):
    for x, row in enumerate(brd):
        for y, col in enumerate(row):
            brd[x][y] = EMPTY

#check if a player has won
def is_winner(brd, player):
    winningStates = [[brd[0][0], brd[0][1], brd[0][2]],
                     [brd[1][0], brd[1][1], brd[1][2]],
                     [brd[2][0], brd[2][1], brd[2][2]],
                     [brd[0][0], brd[1][0], brd[2][0]],
                     [brd[0][1], brd[1][1], brd[2][1]],
                     [brd[0][2], brd[1][2], brd[2][2]],
                     [brd[0][0], brd[1][1], brd[2][2]],
                     [brd[0][2], brd[1][1], brd[2][0]]]

    if [player, player, player] in winningStates:
        return True

    return False

#check if the game has been won
def is_game_over(brd):
    return is_winner(brd, x_player) or is_winner(brd, o_player)

#print the result of the game
def print_game_result(brd):
    if is_winner(brd, x_player):
        print('X won! ' + '\n')

    elif is_winner(brd, o_player):
        print('O\'s won! ' + '\n')

    else:
        print('Draw!' + '\n')

#return a list of empty cells
def get_available_moves(brd):
    emptyC = []
    for x, row in enumerate(brd):
        for y, col in enumerate(row):
            if brd[x][y] == EMPTY:
                emptyC.append([x, y])

    return emptyC

#check if the board is full
def is_board_complete(brd):
    if len(get_available_moves(brd)) == 0:
        return True
    return False

#set move on board
def place_mark(brd, x, y, player):
    brd[x][y] = player

#gets a player's move, validates it, places the mark on the board,
#and prints the updated board and "alpha" and "beta" values.
def get_player_move(brd):
    e = True
    moves = {1: [0, 0], 2: [0, 1], 3: [0, 2],
             4: [1, 0], 5: [1, 1], 6: [1, 2],
             7: [2, 0], 8: [2, 1], 9: [2, 2]}
    while e:
        try:
            move = int(input('Pick a position(1-9)'))
            if move < 1 or move > 9:
                print('Invalid location! ')
            elif not (moves[move] in get_available_moves(brd)):
                print('Location filled')
            else:
                place_mark(brd, moves[move][0], moves[move][1], x_player)
                print_board(brd)
                print("alpha = -inf")
                print("beta = inf")
                e = False
        except(KeyError, ValueError):
            print('Please pick a number!')

#evaluates the outcome of a game or match, returning 10 for an x_player win, -10 for an o_player win, and 0 for a tie.
def evaluate_score(brd):
    if is_winner(brd, x_player):
        return 10

    elif is_winner(brd, o_player):
        return -10

    else:
        return 0

#It simulates future moves, assigns scores and returns the best move
#for the current player using alpha-beta pruning for efficient search.
def minimax_with_alpha_beta(brd, depth, alpha, beta, player):
    row = -1
    col = -1
    alpha_cut = 0
    beta_cut = 0
    if depth == 0 or is_game_over(brd):
        return [row, col, evaluate_score(brd)]

    else:
        for cell in get_available_moves(brd):
            place_mark(brd, cell[0], cell[1], player)
            score = minimax_with_alpha_beta(brd, depth - 1, alpha, beta, -player)
            if player == x_player:
                # X is always the max player
                if score[2] > alpha:
                    alpha = score[2]
                    row = cell[0]
                    col = cell[1]

            else:
                if score[2] < beta:
                    beta = score[2]
                    row = cell[0]
                    col = cell[1]

            place_mark(brd, cell[0], cell[1], EMPTY)
            alpha_cut_check = False

            if alpha >= beta:
                alpha_cut = alpha
                beta_cut = beta
                alpha_cut_check = True
                break

        if player == x_player:
            return [row, col, alpha, beta, alpha_cut_check, alpha_cut, beta_cut]

        else:
            return [row, col, beta, alpha, alpha_cut_check, alpha_cut, beta_cut]

#it chooses a spot either randomly or by using minimax algorithm
#with alpha-beta pruning, then prints the updated board.
def AIMove(brd):
    if len(get_available_moves(brd)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        place_mark(brd, x, y, o_player)
        print_board(brd)

    else:
        result = minimax_with_alpha_beta(brd, len(get_available_moves(brd)), -inf, inf, o_player)
        place_mark(brd, result[0], result[1], o_player)
        print_board(brd)

#makes a move for the AI player using the minimax algorithm with alpha-beta pruning,
#starting with the x_player symbol and using the available moves on the board.
def AI2Move(brd):
    if len(get_available_moves(brd)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        place_mark(brd, x, y, x_player)
        print_board(brd)

    else:
        result = minimax_with_alpha_beta(brd, len(get_available_moves(brd)), -inf, inf, x_player)
        place_mark(brd, result[0], result[1], x_player)
        print_board(brd)

#Runs 1000 games of AI vs AI and prints the number of wins
def AIversusAI():
    currentPlayer = x_player
    count = 0
    for x in range(1000):
        clear_Board(board)

        while not (is_board_complete(board) or is_game_over(board)):
            makeMove(board, currentPlayer, 2)
            currentPlayer *= -1

        print_game_result(board)
        if is_game_over(board):
            count += 1

    print('Number of AI vs AI wins =', count)

#Handles player vs AI or AI vs AI game mode, calls appropriate move function for current player.
def makeMove(brd, player, mode):
    if mode == 1:
        if player == x_player:
            get_player_move(brd)

        else:
            AIMove(brd)
    else:
        if player == x_player:
            AIMove(brd)
        else:
            AI2Move(brd)

#Implements AI move using minimax with alpha-beta pruning for simple game mode.
def AIMoveABForSimple(brd):
    if len(get_available_moves(brd)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        place_mark(brd, x, y, o_player)
        print_board(brd)
        print("alpha = -inf")
        print("beta = inf")

    else:
        result = minimax_with_alpha_beta(brd, 2, -inf, inf, o_player)
        place_mark(brd, result[0], result[1], o_player)
        print_board(brd)
        print("alpha =", result[3])
        print("beta =", result[2])
        if result[4]:
            print("alpha cut ", end = "")  
            print("( alpha_cut =", result[5], end = "")
            print(", beta_cut =", result[6], ")") 
def makeMoveForSimple(brd, player, mode):
    if mode == 1:
        if player == x_player:
            get_player_move(brd)

        else:
            AIMoveABForSimple(brd)

#Simple or hard mode,and who goes first,game logic for each mode
def playerVSai():
    print("Do you want to play simple or hard? (1/2)")
    mode = int(input())
    if mode == 1:
        while True:
            try:
                print("Would you like to go first or second? (1/2)")
                order = int(input())
                if not (order == 1 or order == 2):
                    print("Please pick 1 or 2")
                else:
                    break
            except(KeyError, ValueError):
                print("Enter a number")

        clear_Board(board)
        if order == 2:
            currentPlayer = o_player
        else:
            currentPlayer = x_player

        while not (is_board_complete(board) or is_game_over(board)):
            makeMoveForSimple(board, currentPlayer, 1)
            currentPlayer *= -1

        print_game_result(board)
    else: 
        while True:
            try:
                print("Would you like to go first or second? (1/2)")
                order = int(input())
                if not (order == 1 or order == 2):
                    print("Please pick 1 or 2")
                else:
                    break
            except(KeyError, ValueError):
                print("Enter a number")

        clear_Board(board)
        if order == 2:
            currentPlayer = o_player
        else:
            currentPlayer = x_player

        while not (is_board_complete(board) or is_game_over(board)):
            makeMove(board, currentPlayer, 1)
            currentPlayer *= -1

        print_game_result(board)

#A game loop for playing against AI, exits on 'N' input.
def main():
    while True:
        user = input('Wanna Play?(Y/N) ')
        if user.lower() == 'y':
            n = input('AI versus AI or Player vursus AI(1/2)')
            if int(n) == 1:
                AIversusAI()
            else:
                playerVSai()
        else:
            print('GG')
            exit()


if __name__ == '__main__':
    main()
