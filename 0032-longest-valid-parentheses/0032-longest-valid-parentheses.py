class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # -1 handles the edge case for the first valid substring
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                
                if not stack:
                    # empty stack, the current ) has no match
                    # push current as the new base for the next valid
                    stack.append(i)
                else:
                    # valid pair found -> calculate length from last unmatched
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len