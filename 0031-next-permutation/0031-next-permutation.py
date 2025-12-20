class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # scan backwards to find the dip
        # lookign for first elem thats smaller than neighbor
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # if i is -1, whole thing is desc sorted so skip this
        if i >= 0:
            j = n - 1
            # find the num just bigger than pivot to swap with
            # start from end again
            while nums[j] <= nums[i]:
                j -= 1
            
            # swap em
            nums[i], nums[j] = nums[j], nums[i]
        
        # reverse the rest of the list... making it ascending
        # if i is -1 this handles the whole list reversal case
        l = i + 1
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l] # flip
            l += 1
            r -= 1