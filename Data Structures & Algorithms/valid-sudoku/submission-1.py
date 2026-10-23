class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset = set()

        #checks rows
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in hashset:
                    return False
                hashset.add(board[row][col])
            hashset.clear()

        #checks cols
        for col in range(len(board)):
            for row in range(len(board)):
                if board[row][col] == ".":
                    continue
                if board[row][col] in hashset:
                    return False
                hashset.add(board[row][col])
            hashset.clear()

        #checks boxes
        #   - check first 3 cols and 3 rows, then next 3x3
        #   - from starting part, check 3 to the right and 3 down
        startrow = 0
        startcol = 0
        for r in range(3):
            for c in range(3):
                if not self.helper(startrow, startcol, board):
                    return False
                startcol += 3
            startcol = 0
            startrow += 3
        return True

    def helper(self, startrow, startcol, board) -> bool:
        hashset = set()
        row = startrow
        col = startcol
        for r in range(3):
            for c in range(3):
                if board[row][col] == ".":
                    col += 1
                    continue
                if board[row][col] in hashset:
                    return False
                hashset.add(board[row][col])
                col += 1
            col = startcol
            row += 1
        return True
            
            



        