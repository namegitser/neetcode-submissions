class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row_check(board):
            
            for i in range(0,9):
                checker = set()
                for j in range(0,9):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in checker:
                        return False

                    checker.add(board[i][j])

            return True
                
        def col_check(board):
            for i in range(0,9):
                checker = set()
                for j in range(0,9):
                    if board[j][i] == '.':
                        continue
                    if board[j][i] in checker:
                        return False

                    checker.add(board[j][i])

            return True

        def mat_check(board):
            for square in range(0,9):
                seen = set()
                for i in range(0,3):
                    for j in range(0,3):
                        row = (square//3)*3 + i
                        col = (square%3)*3 + j
                        if board[row][col] == '.':
                            continue
                        if board[row][col] in seen:
                            return False

                        seen.add(board[row][col])

            return True

        return row_check(board) and col_check(board) and mat_check(board)

