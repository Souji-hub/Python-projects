class GameOfLife:  # making a class game of life
    def __init__(self, n):  #constructor initialization
        self.n = n
        self.board = [[0] * n for _ in range(n)]  #making a board of nxn

    def neighbourSum(self, i, j):  #calculating neighbour sum
        n = self.n
        neighbours = [
            self.board[(i - 1 + n) % n][(j - 1 + n) % n],
            self.board[(i - 1 + n) % n][j],
            self.board[(i - 1 + n) % n][(j + 1) % n],
            self.board[i % n][(j + 1) % n],
            self.board[(i + 1) % n][(j + 1) % n],
            self.board[(i + 1) % n][j],
            self.board[(i + 1) % n][(j - 1 + n) % n],
            self.board[i][(j - 1 + n) % n]
        ]
        return sum(neighbours)

    def nextPattern(self):  # calculating if the cell is alive or dead using the conditions of gameoflife
        n = self.n
        newBoard = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                cell = self.board[i][j]
                neighbours = self.neighbourSum(i, j)

                if cell == 1:
                    if neighbours < 2 or neighbours > 3:
                        newBoard[i][j] = 0
                    else:
                        newBoard[i][j] = 1
                else:
                    if neighbours == 3:
                        newBoard[i][j] = 1
        self.board = newBoard

    def printBoard(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    print(" ", end="")
                else:
                    print("*", end="")
            print()

def main():
    # Create initial patterns
    pattern1 = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1]
    ]

    pattern2 = [
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1]
    ]

    pattern3 = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    patterns = [pattern1, pattern2, pattern3]

    # Initialize the game
    n = 20
    game = GameOfLife(n)

    # Print initial patterns and ask for user choice
    print("Choose a pattern to play with:")
    for i, pattern in enumerate(patterns):
        print(f"Pattern {i + 1}:")
        for row in pattern:
            for cell in row:
                if cell == 0:
                    print(" ", end="")
                else:
                    print("*", end="")
            print()
        print()

    choice = int(input("Enter the pattern number: "))
    chosen_pattern = patterns[choice - 1]

    # Set chosen pattern on the game board
    for i in range(len(chosen_pattern)):
        for j in range(len(chosen_pattern[i])):
            game.board[i][j] = chosen_pattern[i][j]

    # Start the game
    while True:
        game.printBoard()
        print("Enter 'q' to quit or any other key to continue.")
        user_input = input()
        if user_input == 'q':
            break
        game.nextPattern()

if __name__ == '__main__':
    main()