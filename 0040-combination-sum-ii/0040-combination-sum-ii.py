class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(start, path, remainder):
            if remainder == 0:
                res.append(path)
                return
            
            for i in range(start, len(candidates)):
                curr = candidates[i]
                
                # if curr is bigger than rem, nothin else will work
                if curr > remainder:
                    break
                
                # if its same as prev number in this loop, skip to avoid duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # recurse with i+1 cuz we cant reuse same element
                dfs(i + 1, path + [curr], remainder - curr)

        dfs(0, [], target)
        return res