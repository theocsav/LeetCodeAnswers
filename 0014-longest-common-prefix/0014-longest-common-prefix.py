class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        i = 0
        first = strs[0]
        last = strs[-1]
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]