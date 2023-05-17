def printBoard(board):
    for key in board:
        print(board[key] + '|' + board[key] + '|' + board[key])
        if key != 'C3':  # Add a condition to avoid printing the separator after the last row
            print('-+-+-')
board = {'A1': 'X', 'A2': 'O', 'A3': 'X', 'B1': 'O', 'B2': 'X', 'B3': 'O', 'C1': 'X', 'C2': 'O', 'C3': 'X'}
printBoard(board)