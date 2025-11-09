class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}

        for i, num in enumerate(nums):
            if num in seen:
                prev = seen[num]
                if i - prev <= k:
                    return True

            seen[num] = i

        return False
        