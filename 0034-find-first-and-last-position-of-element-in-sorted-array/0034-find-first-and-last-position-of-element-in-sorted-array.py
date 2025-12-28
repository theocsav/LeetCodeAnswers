class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # binary search helper
        # findLeft is bool to switch direction
        def binSearch(findLeft):
            l, r = 0, len(nums) - 1
            idx = -1
            
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    # found target, save index
                    idx = mid
                    # if checking left, squeeze r to find start
                    if findLeft:
                        r = mid - 1
                    else:
                        l = mid + 1
            return idx

        # get start pos
        start = binSearch(True)
        
        # optimization: if start is -1 target isnt there
        if start == -1:
            return [-1, -1]
            
        # get end pos
        end = binSearch(False)
        
        return [start, end]