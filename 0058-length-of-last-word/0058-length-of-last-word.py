class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        data = s.strip().split()
        if len(data) == 0:
            return "0"
        return len(data[-1])

        