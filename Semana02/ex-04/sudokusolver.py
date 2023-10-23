def solve_sudoku(board):
    # Encontre a próxima célula vazia
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Nenhum espaço vazio, o Sudoku está resolvido

    row, col = empty_cell

    # Tente números de 1 a 9
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            # Recursivamente tente preencher o restante do tabuleiro
            if solve_sudoku(board):
                return True

            # Se não for possível, volte e tente outro número
            board[row][col] = 0

    return False  # Não há solução para o Sudoku

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid_move(board, row, col, num):
    # Verifique a linha
    if num in board[row]:
        return False

    # Verifique a coluna
    if num in [board[i][col] for i in range(9)]:
        return False

    # Verifique o quadrante 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

# Exemplo de um tabuleiro Sudoku (0 representa células vazias)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Sudoku resolvido:")
    print_sudoku(sudoku_board)
else:
    print("Não há solução para o Sudoku.")

