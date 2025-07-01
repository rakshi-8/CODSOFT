import math

player = "X"  # Human
ai = "O"      # AI
board = [" " for _ in range(9)]  # 3x3 Board

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for cond in win_conditions:
        if all(brd[i] == player for i in cond):
            return True
    return False

def minimax(brd, depth, is_maximizing):
    if winner(brd, ai):
        return 1
    elif winner(brd, player):
        return -1
    elif " " not in brd:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in available_moves():
            brd[i] = ai
            score = minimax(brd, depth + 1, False)
            brd[i] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in available_moves():
            brd[i] = player
            score = minimax(brd, depth + 1, True)
            brd[i] = " "
            best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in available_moves():
        board[i] = ai
        score = minimax(board, 0, False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    board[move] = ai

def main():
    print("Tic Tac Toe Game - You vs AI")
    print_board()

    while True:
        # Human move
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] != " ":
                print("Invalid move. Try again.")
                continue
            board[move] = player
        except:
            print("Invalid input. Enter number between 0-8.")
            continue

        print_board()

        if winner(board, player):
            print("You win!")
            break
        elif " " not in board:
            print("It's a draw!")
            break

        # AI move
        best_move()
        print("AI moved:")
        print_board()

        if winner(board, ai):
            print("AI wins!")
            break
        elif " " not in board:
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
