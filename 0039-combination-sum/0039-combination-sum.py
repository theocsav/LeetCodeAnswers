class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # sort first so we can break erly if nums get too big
        candidates.sort()
        
        def dfs(rem, start, path):
            if rem == 0:
                # bingo, found a valid combo
                res.append(path)
                return
            
            for i in range(start, len(candidates)):
                curr = candidates[i]
                
                # if curr num is bigger than remainder, rest wont work either
                if curr > rem:
                    break
                
                # recurse... pass i again bc we can resue same number
                dfs(rem - curr, i, path + [curr])
                
        dfs(target, 0, [])
        return res