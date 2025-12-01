class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def k_sum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    if nums[i] * k > target or nums[-1] * k < target:
                        break
                    if nums[i] + nums[-1] * (k - 1) < target:
                        continue
                    
                    for subset in k_sum(k - 1, i + 1, target - nums[i]):
                        yield [nums[i]] + subset
            else:
                l, r = start, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        yield [nums[l], nums[r]]
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

        return list(k_sum(4, 0, target))