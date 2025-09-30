def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")
    print()

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   
        [0, 4, 8], [2, 4, 6]               
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):  # AI wins
        return 1
    elif check_winner(board, "X"):  # Human wins
        return -1
    elif " " not in board:  # Draw
        return 0

    if is_maximizing:  # AI's turn
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:  # Human's turn
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [" " for _ in range(9)]
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board(board)

    while True:
        # Human move
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue
            board[move] = "X"
        except ValueError:
            print("Please enter a valid number between 0 and 8.")
            continue

        print_board(board)

        if check_winner(board, "X"):
            print("🎉 Rishu Won!")
            break
        if " " not in board:
            print("🤝 It's a Draw!")
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = "O"
        print("AI chooses position", ai_move)
        print_board(board)

        if check_winner(board, "O"):
            print("💻 AI Won!")
            break
        if " " not in board:
            print("🤝 It's a Draw!")
            break


if __name__ == "__main__":
    play_game()
