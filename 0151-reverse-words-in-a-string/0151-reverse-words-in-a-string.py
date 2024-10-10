class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split()
        print(ls)
        return " ".join(ls[::-1])