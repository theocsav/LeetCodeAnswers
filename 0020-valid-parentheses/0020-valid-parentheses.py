class Solution:
    def isValid(self, s: str) -> bool:
        bMap = {')': '(', '}': '{', ']': '['}
        
        stack = []
        
        for char in s:
            if char in bMap:
                top = stack.pop() if stack else '&'
                
                if bMap[char] != top:
                    return False
            else:
                stack.append(char)
                
        return not stack