# Step 1: Design the game board as a 3x3 list of lists
board = [[" " for _ in range(3)] for _ in range(3)]

# Step 2: Create a function to print the game board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Step 3: Create a function to handle player moves
def get_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

# Step 4: Create a function to check for a win
def check_win(board, player):
    # Check rows
    for row in board:
        if all(square == player for square in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Step 5: Create a function to check for a tie
def check_tie(board):
    return all(square != " " for row in board for square in row)

# Step 6 and 7: Create the main game loop
def main():
    current_player = "X"
    while True:
        print_board(board)
        row, col = get_move(current_player)
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"

# Step 8: Test the game
if __name__ == "__main__":
    main()
