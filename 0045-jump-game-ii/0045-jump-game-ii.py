class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # loop til the second to last element
        for i in range(len(nums) - 1):
            
            # update the furthest we can go from here
            farthest = max(farthest, i + nums[i])
            
            # if we reached the end of the currrent jump scope
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps