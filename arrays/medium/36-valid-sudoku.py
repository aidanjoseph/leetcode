'''
not the pretteist solution kidna ugly
coudl do better
'''
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #hashmap --> key: (r,c), --> num

        pos = defaultdict(int) 
        def checkCol(row, num):
            for col in range(0, cols):
                if pos[(row, col)] == num:
                    return True
            return False
        def checkRow(col, num):
            for row in range(0, rows):
                if pos[(row, col)] == num:
                    return True
            return False
        def checkThree(row, col, num):
            r = row - (row % 3)
            c = col - (col % 3)
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if pos[(i, j)] == num:
                        return True
            return False
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != ".":
                    num = board[r][c]
                    if checkCol(r, num) or checkRow(c, num) or checkThree(r, c, num):
                        return False
                    pos[(r, c)] = num
        return True
        '''
        Ideal better solution
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True
        '''
                    

