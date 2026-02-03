class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # rows as sets for fast lookup
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        res = []
        for w in words:
            low_w = set(w.lower())
            
            # check if the word's letters are entirely within any row
            if low_w <= row1 or low_w <= row2 or low_w <= row3:
                res.append(w)
                
        return res