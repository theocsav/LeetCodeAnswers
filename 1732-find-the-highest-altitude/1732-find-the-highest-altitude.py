class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        highest = 0
        
        for g in gain:
            curr += g
            highest = max(highest, curr)
            
        return highest