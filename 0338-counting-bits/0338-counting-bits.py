class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # use previous results
            # i >> 1 shifs right
            # i & 1 checks if it's odd or even
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans