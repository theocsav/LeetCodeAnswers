class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)] 
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == '.':
                    continue
                
                # calc box index. 
                # r=0-2, c=0-2 is box 0. r=8, c=8 is box 8
                b_idx = (r // 3) * 3 + (c // 3)
                
                # check if we seen this num b4 in row, col or box
                if val in rows[r]:
                    return False
                if val in cols[c]:
                    return False
                if val in boxes[b_idx]:
                    return False # duplicate found
                
                # add to tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[b_idx].add(val)
        
        return True