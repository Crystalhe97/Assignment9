class Board:
    def __init__(self):
    # Initialize the board with empty cells
        self.__rows = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]


    def __str__(self):
    # Generate a string representation of the board for display
        s = '-------\n'
        for row in self.__rows:
            for cell in row:
                s = s + '|'
                if cell == None:
                    s=s+' '
                else:
                    s=s+cell
            s = s + '|\n-------\n'
        return s


    def get(self, x, y):
    # Get the value at a specific position on the board
        return self.__rows[y][x]


    def set(self, x, y, value):
    # Set a value at a specific position on the board
        if x >= len(self.__rows[0]) or y >= len(self.__rows):
            print(f"out of bounds, try again\n")
            raise ValueError
        if self.__rows[y][x]:
            print(
                f"{y},{x} already has mark {self.__rows[y][x]}, please choose another place\n"
            )
            raise ValueError
        self.__rows[y][x] = value


    def check_winner(self):
        for row in self.__rows:
            if len(set(row)) == 1:
                return row[0]

        # check columns
        #    ['X', 'X', 'X'],
        #    ['O', 'X', 'O'],
        #    ['O', 'O', 'X'],
        # how to index -> board[row][column]
        # column_idxs = [[0,0], [1,0], [2,0]]
        # column_idxs = [[0,1], [1,1], [2,1]]
        for i in range(len(self.__rows)):
            # len(board) -> 3
            column = [self.__rows[j][i] for j in range(len(self.__rows))]
            # column => ['X', 'O', 'O']
            # column => ['X', 'X', 'O]
            if len(set(column)) == 1:
                return self.__rows[0][i]

        # check diagonals
        # check columns
        #    ['X', 'X', 'X'],
        #    ['O', 'X', 'O'],
        #    ['O', 'O', 'X'],
        # how to index -> board[row][column]
        # idx -> [[0,0], [1,1], [2, 2]]
        top_left_to_bottom_right = [self.__rows[i][i] for i in range(len(self.__rows))]
        if len(set(top_left_to_bottom_right)) == 1:
            return self.__rows[0][0]

        # check diagonals
        # check columns
        #    ['X', 'X', 'X'],
        #    ['O', 'X', 'O'],
        #    ['O', 'O', 'X'],
        # how to index -> board[row][column]
        # idx -> [[0,2], [1,1], [2, 0]]
        top_right_to_bottom_left = [self.__rows[i][len(self.__rows)-i-1] for i in range(len(self.__rows))]
        if len(set(top_right_to_bottom_left)) == 1:
            return self.__rows[0][len(self.__rows)-1]

        # Check draw
        """
        board = [
            ['O', None, None],
            [None, None, None],
            [None, 'X'', None],
        ]
        # if no None in the board, return draw
        """
        #[2,2].append([1,1]) -> [2,2 [1,1]]
        #[2,2].extend([1,1]) -> [2,2,1,1]
        #flat_board = ["O", "X", "O", "O", "X", "O", "O", "X", "O",]
        flat_board = []
        for row in self.__rows:
            flat_board.extend(row)
        if not None in flat_board:
        #game still in play
            return "draw"
        return None