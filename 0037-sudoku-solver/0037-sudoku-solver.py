class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        self.empty = []
        
        # pre-process board
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    self.empty.append((r, c))
                else:
                    char = board[r][c]
                    self.rows[r].add(char)
                    self.cols[c].add(char)
                    
                    # check 3x3 subbox
                    box_idx = (r // 3) * 3 + (c // 3)
                    self.boxes[box_idx].add(char)
        
        self.solve(board, 0)
    
    def solve(self, board, idx):
        # if all empty cells filled
        if idx == len(self.empty):
            return True
            
        r, c = self.empty[idx]
        box_idx = (r // 3) * 3 + (c // 3)
        
        # try digits 1-9
        for char in "123456789":
            if self.isValid(r, c, box_idx, char):
                board[r][c] = char
                self.rows[r].add(char)
                self.cols[c].add(char)
                self.boxes[box_idx].add(char)
                
                if self.solve(board, idx + 1):
                    return True
                
                # else backtrack
                self.rows[r].remove(char)
                self.cols[c].remove(char)
                self.boxes[box_idx].remove(char)
                board[r][c] = '.'
                
        return False

    def isValid(self, r, c, box_idx, char):
        # check row and column and subbox
        if char in self.rows[r] or char in self.cols[c] or char in self.boxes[box_idx]:
            return False
            
        return True