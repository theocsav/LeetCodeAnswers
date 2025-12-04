class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(index, current_str):
            if len(current_str) == len(digits):
                res.append(current_str)
                return
        
            current_digit = digits[index]
            possible_letters = phone_map[current_digit]

            for letter in possible_letters:
                backtrack(index + 1, current_str + letter)
    
        backtrack(0, "")

        return res