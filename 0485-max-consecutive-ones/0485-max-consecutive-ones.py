class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        cur = 0
        
        for n in nums:
            if n == 1:
                cur += 1
                # keep track of the biggest streak
                best = max(best, cur)
            else:
                cur = 0
                
        return best