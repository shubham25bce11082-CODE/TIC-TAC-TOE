import math

def show_board(board):
    for i in range(3):
        print(board[i][0], "|", board[i][1], "|", board[i][2])
        if i < 2:
            print("--+---+--")
    print()


# Checking if someone has won
def check_winner(board):
    # Rows, columns, diagonals
    lines = []

    lines.extend(board)  # rows

    # columns
    for col in range(3):
        lines.append([board[0][col], board[1][col], board[2][col]])

    # diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != " ":
            return line[0]

    return None


# Check if the board is full
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True


# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)

    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score


# Find best move for AI
def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move


# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("You are X, AI is O\n")

    while True:
        show_board(board)

        # Player move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))

                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken")
            except:
                print("Invalid input")

        # Check after player move
        if check_winner(board) == "X":
            show_board(board)
            print("You win!")
            break

        if is_full(board):
            show_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"

        # Check after AI move
        if check_winner(board) == "O":
            show_board(board)
            print("AI wins!")
            break

        if is_full(board):
            show_board(board)
            print("It's a draw!")
            break


# Run the game
play_game()