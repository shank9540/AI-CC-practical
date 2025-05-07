def n_queens(n):
    board = [[0] * n for _ in range(n)]
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def print_board():
        for row in board:
            print(" ".join("Q" if cell else "." for cell in row))
        print()

    def backtrack(row):
        if row == n:
            print("Solution:")
            print_board()
            return True
        for col in range(n):
            if not cols[col] and not diag1[row - col + n - 1] and not diag2[row + col]:
                board[row][col] = 1
                cols[col] = diag1[row - col + n - 1] = diag2[row + col] = True
                if backtrack(row + 1):
                    return True  # To get all solutions, remove this line
                board[row][col] = 0
                cols[col] = diag1[row - col + n - 1] = diag2[row + col] = False
        return False

    print(f"\nSolving N-Queens for N = {n}")
    if not backtrack(0):
        print("No solution found.")


def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n

    def is_safe(node, c):
        for neighbor in range(n):
            if graph[node][neighbor] == 1 and color[neighbor] == c:
                return False
        return True

    def backtrack(node):
        if node == n:
            return True
        for c in range(1, m + 1):
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False

    print(f"\nSolving Graph Coloring with {m} colors")
    if backtrack(0):
        print("Color Assignment:", color)
    else:
        print("No solution exists with", m, "colors.")


# User Choice
def main():
    print("Constraint Satisfaction Problem Solver")
    print("1. N-Queens Problem")
    print("2. Graph Coloring Problem")
    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        n = int(input("Enter number of queens (N): "))
        n_queens(n)
    elif choice == 2:
        print("Example graph with 4 nodes:")
        graph = [
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        m = int(input("Enter number of colors: "))
        graph_coloring(graph, m)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
