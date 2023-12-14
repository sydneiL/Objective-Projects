class CheckerboardGame:
    def __init__(self):
        self.board_size = 8
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.populate_board()

    def populate_board(self):
        # Populate the initial positions of black and white pieces
        for row in range(3):
            for col in range(self.board_size):
                if (row + col) % 2 == 1:
                    self.board[row][col] = 'B'

        for row in range(5, self.board_size):
            for col in range(self.board_size):
                if (row + col) % 2 == 1:
                    self.board[row][col] = 'W'

    def print_board(self):
        # Print the current state of the checkerboard
        for row in self.board:
            print(' '.join(row))
        print()

    def is_valid_move(self, start, end):
        # Check if the move is valid based on the current state of the board
        start_row, start_col = start
        end_row, end_col = end

        if (
            0 <= start_row < self.board_size and
            0 <= start_col < self.board_size and
            0 <= end_row < self.board_size and
            0 <= end_col < self.board_size
        ):
            if self.board[start_row][start_col] != ' ' and self.board[end_row][end_col] == ' ':
                return True

        return False

    def make_move(self, start, end):
        # Make a move on the board
        start_row, start_col = start
        end_row, end_col = end

        if self.is_valid_move(start, end):
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = ' '
            return True
        else:
            return False


def main():
    game = CheckerboardGame()

    while True:
        game.print_board()

        # Get user input for the move
        start_row = int(input("Enter the row number of the piece to move: "))
        start_col = int(input("Enter the column number of the piece to move: "))
        end_row = int(input("Enter the row number to move the piece to: "))
        end_col = int(input("Enter the column number to move the piece to: "))

        move = ((start_row, start_col), (end_row, end_col))

        # Make the move and check if it's valid
        if game.make_move(*move):
            print("Move successful!")
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()