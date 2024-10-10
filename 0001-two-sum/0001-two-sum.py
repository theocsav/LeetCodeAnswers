class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # LeetHub
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[j] == target - nums[i]:
                    return [i, j]