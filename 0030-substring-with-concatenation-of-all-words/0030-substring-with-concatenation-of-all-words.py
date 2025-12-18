from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        
        # basic setup
        cnt = Counter(words)
        n, m = len(s), len(words[0])
        k = len(words)
        res = []

        # offset loop
        for i in range(m):
            cur = Counter()
            left = i
            
            # slide right window
            for j in range(i, n - m + 1, m):
                word = s[j : j + m]
                
                if word in cnt:
                    cur[word] += 1
                    
                    # if 2 many words, shrink left
                    while cur[word] > cnt[word]:
                        cur[s[left : left + m]] -= 1
                        left += m
                    
                    # exact match found
                    if j + m - left == k * m:
                        res.append(left)
                
                else:
                    # bad word. reset window
                    cur.clear()
                    left = j + m
                    
        return res