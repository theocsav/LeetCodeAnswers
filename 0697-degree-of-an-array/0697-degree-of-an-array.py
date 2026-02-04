class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_seen = {}
        last_seen = {}
        counts = {}
        
        for i, x in enumerate(nums):
            # store first spot we see it
            if x not in first_seen:
                first_seen[x] = i
            # always update last spot
            last_seen[x] = i
            # bump up the count
            counts[x] = counts.get(x, 0) + 1
            
        degree = max(counts.values())
        # start with a big number for min length
        ans = len(nums)
        
        for x in counts:
            if counts[x] == degree:
                # find smallest distnce for the peak elements
                length = last_seen[x] - first_seen[x] + 1
                if length < ans:
                    ans = length
                    
        return ans