def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def backtrack(row):
        if row == n:
            print_solution(board)
            return True  # Return True for one solution; for all, remove this line
        for col in range(n):
            if not cols[col] and not diag1[row - col + n - 1] and not diag2[row + col]:
                board[row][col] = 1
                cols[col] = diag1[row - col + n - 1] = diag2[row + col] = True
                if backtrack(row + 1):
                    return True
                board[row][col] = 0
                cols[col] = diag1[row - col + n - 1] = diag2[row + col] = False
        return False

    if not backtrack(0):
        print("No solution found.")

# Example:
print("N-Queens (4x4):")
solve_n_queens(4)
