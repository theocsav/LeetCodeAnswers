class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i, interval in enumerate(intervals):
            # curr ends before new one starts
            if interval[1] < newInterval[0]:
                res.append(interval)
            
            # curr starts after new one ends
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                # just returm the rest since its sorted
                return res + intervals[i:]
            
            # overlap
            else:
                # expand the new interval to cover both
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        # append the new one if we finished loop witout returning
        res.append(newInterval)
        
        return res