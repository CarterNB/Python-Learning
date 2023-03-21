def find_next_empty(puzzle):
    # Find next row,col on the puzzle that is not solved
    # return row,col tuple or (None, None) once the puzzle is solved

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None


def is_valid(puzzle, guess, row, col):
    # if value has already been guessed in the row, False
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # For the guess, if the number has not shown up in the row yet check if number is in column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Iterating over each 3x3 section of puzzle
    row_start = (row // 3) * 3  # 1//3=0, 5//3=1,..... therefore check row 0,1,2 and col 0,1,2 values etc.
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    # If guess does not contain the same number in the row, column, or 3x3 square
    return True


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    # Puzzle has no empty squares left
    if row is None:
        return True
    #for values between 1 and 9 insert into each of the 81 squares and check if the value is valid
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle): #if guess is correct
                return True

        # if puzzle is not solved by this guess (invalid guess), reset guess and try new number until valid
        puzzle[row][col] = -1

    return False


if __name__ == '__main__':
    example_board = [
        [4, -1, 6, 7, -1, -1, -1, 8, 5],
        [-1, 8, -1, -1, -1, -1, 9, -1, -1],
        [-1, -1, -1, -1, 5, -1, 1, -1, -1],

        [3, -1, -1,9, -1, -1,-1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 1],
        [-1, 4, -1, -1, 3, -1, -1, 5, 6],

        [-1, 6, -1, -1, 9, -1, -1, 4, 3],
        [-1, -1, -1, -1, -1, -1, 8, -1, -1],
        [-1, -1, 7, -1, -1, 2, -1, -1, -1],
    ]

    print(solve_sudoku(example_board))
    for i in range(9):
        print(example_board[i])
