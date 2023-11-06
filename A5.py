class NQBacktracking:
    def __init__(self, x_, y_):
        self.ld = [0] * (2 * N - 1)
        self.rd = [0] * (2 * N - 1)
        self.cl = [0] * N
        self.x = x_
        self.y = y_

    def printSolution(self, board):
        print("N Queen Backtracking Solution:")
        for line in board:
            print(" ".join(map(str, line)))

    def solveNQUtil(self, board, col):
        if col >= N:
            return True

        if col == self.y:
            return self.solveNQUtil(board, col + 1)

        for i in range(N):
            if i == self.x:
                continue

            if (self.ld[i - col + N - 1] != 1 and self.rd[i + col] != 1) and self.cl[i] != 1:
                board[i][col] = 1
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 1

                if self.solveNQUtil(board, col + 1):
                    return True

                board[i][col] = 0
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 0

        return False

    def solveNQ(self):
        board = [[0 for _ in range(N)] for _ in range(N)]
        board[self.x][self.y] = 1
        self.ld[self.x - self.y + N - 1] = self.rd[self.x + self.y] = self.cl[self.x] = 1

        if not self.solveNQUtil(board, 0):
            print("Solution does not exist")
            return False
        self.printSolution(board)
        return True


if __name__ == "__main__":
    N = int(input("Enter the size of the chessboard (N): "))
    x = int(input("Enter the row position (0 to N-1) of the first queen: "))
    y = int(input("Enter the column position (0 to N-1) of the first queen: "))

    if x < 0 or x >= N or y < 0 or y >= N:
        print("Invalid initial position for the first queen.")
    else:
        NQBt = NQBacktracking(x, y)
        NQBt.solveNQ()
