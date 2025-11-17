import re
class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'^\s*([+-]?\d+)', s)

        if not match:

            return 0
        
        result = int(match.group(1))

        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        return max(INT_MIN, min(result, INT_MAX))