# Tic Tac Toe with Minimax AI and Multiplayer Option + Player Name Input + Victory Message

board = [' ' for _ in range(9)]
win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],   # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],   # Columns
    [0, 4, 8], [2, 4, 6]               # Diagonals
]

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def is_winner(board, player):
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def get_empty_squares(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def can_win(board, player):
    for condition in win_conditions:
        values = [board[i] for i in condition]
        if all(v == player or v == ' ' for v in values):
            return True
    return False

def is_unwinnable(board):
    return not can_win(board, 'X') and not can_win(board, 'O')

def player_move(player_name, player_symbol):
    while True:
        try:
            move = int(input(f"{player_name} ({player_symbol}), enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = player_symbol
                break
            else:
                print("Invalid move. Please choose an empty square from 1 to 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ai_move():
    best_score = -float('inf')
    best_move = None
    for move in get_empty_squares(board):
        board[move] = 'O'
        score = minimax(board, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    
    board[best_move] = 'O'
    print("AI chose move:", best_move + 1)

def minimax(board, is_maximizing):
    if is_winner(board, 'O'):
        return 10
    if is_winner(board, 'X'):
        return -10
    if is_unwinnable(board) or is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_empty_squares(board):
            board[move] = 'O'
            score = minimax(board, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_empty_squares(board):
            board[move] = 'X'
            score = minimax(board, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def play_vs_computer(player_name):
    print(f"\nWelcome {player_name}! You are 'X'. Let's play vs Computer 🤖\n")
    print_board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    while True:
        player_move(player_name, 'X')
        print_board(board)
        if is_winner(board, 'X'):
            print(f"🎉 Congratulations {player_name}, you defeated the AI! 🏆")
            print("Victory Message: You outsmarted the computer! 👑")
            break
        if is_unwinnable(board) or is_board_full(board):
            print("🤝 It's a draw! Well played!")
            break

        print("AI is thinking...")
        ai_move()
        print_board(board)
        if is_winner(board, 'O'):
            print("🤖 AI wins! Better luck next time!")
            print("Victory Message: The machine prevails this time! ⚙️")
            break
        if is_unwinnable(board) or is_board_full(board):
            print("🤝 It's a draw! Well played!")
            break

def play_multiplayer(player1_name, player2_name):
    print(f"\nWelcome {player1_name} (X) and {player2_name} (O)! Let's play!\n")
    print_board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    current_player = 'X'
    current_name = player1_name

    while True:
        player_move(current_name, current_player)
        print_board(board)
        if is_winner(board, current_player):
            print(f"🎉 {current_name} wins the match! 🏆")
            print(f"Victory Message: Outstanding game, {current_name}! 👑")
            break
        if is_unwinnable(board) or is_board_full(board):
            print("🤝 It's a draw! Great match between both players!")
            break
        # Switch players
        if current_player == 'X':
            current_player = 'O'
            current_name = player2_name
        else:
            current_player = 'X'
            current_name = player1_name

def play_game():
    print("Welcome to Tic-Tac-Toe!\n")
    print("Choose a mode:")
    print("1. Play vs Computer")
    print("2. Play Multiplayer")

    while True:
        mode = input("Enter your choice (1 or 2): ")
        if mode == '1':
            player_name = input("Enter your name: ")
            play_vs_computer(player_name)
            break
        elif mode == '2':
            player1_name = input("Enter name for Player 1: ")
            player2_name = input("Enter name for Player 2: ")
            play_multiplayer(player1_name, player2_name)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    play_game()
