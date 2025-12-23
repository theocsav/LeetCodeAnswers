class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # init ptrs
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # chk if left half is sorted
            if nums[l] <= nums[mid]:
                # if atrget is in bounds of left
                if nums[l] <= target < nums[mid]:
                    r = mid - 1 # cut rght
                else:
                    l = mid + 1 # search rght
            # right half must be sorted
            else:
                # if target in bounds of right
                if nums[mid] < target <= nums[r]:
                    l = mid + 1 # cut lft
                else:
                    r = mid - 1 # search lft
                    
        return -1