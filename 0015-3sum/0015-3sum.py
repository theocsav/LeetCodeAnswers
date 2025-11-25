from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = set()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            a = nums[i]
            target = -a
            seen = set()

            for b in nums[i + 1:]:
                c = target - b
                if c in seen:
                    triplets.add((a, c, b))
                seen.add(b)
        
        return [list(t) for t in triplets]