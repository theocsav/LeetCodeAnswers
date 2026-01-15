class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort so duplicates are adjacent
        nums.sort()
        res = []
        
        def backtrack(start, path):
            # add the current subset
            res.append(path)
            
            for i in range(start, len(nums)):
                # if this is a duplicate of the previous number
                # at the start of this recursion level, skip it
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                # move to next index, add current number to path
                backtrack(i + 1, path + [nums[i]])
        
        backtrack(0, [])
        return res