Tic-Tac-Toe Game

This is a Tic-Tac-Toe game that allows for player versus AI gameplay. The AI uses the minimax algorithm with alpha-beta pruning to determine its move.

How to Play

#pip install colorama
1.Run the script
2.Select mode 1 for player versus AI or mode 2 for AI versus AI
3.Follow the prompts to make your move as the player
4.The game will continue until a winner is determined or it results in a draw

Dependencies

The script requires the 'random' and 'math' libraries to run.

Functionality

The script includes several functions that handle different aspects of the game:

. 'get_player_move': Prompts the user to make a move on the board and places the player's mark on the selected spot
. 'evaluate_score': Evaluates the score of the board, returns 10 if X wins, -10 if O wins, 0 if it's a draw
. 'minimax_with_alpha_beta': Uses the minimax algorithm with alpha-beta pruning to determine the best move for the AI
. 'AIMove' and 'AI2Move': Allows for games between two AI players
. 'AIversusAI': Plays 1000 games between two AIs and counts the number of wins
. 'makeMove': Serves as a wrapper function to call either the player move function or the AI move function depending on the mode
. 'place_mark', 'get_available_moves', 'is_winner', 'is_game_over', 'print_board', 'clear_Board', 'print_game_result' are also defined but not shown in the code, they are probably used throughout the script.

Author

This Tic-Tac-Toe game was developed by Hossein Shams as a final project.
