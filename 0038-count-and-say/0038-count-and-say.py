class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        
        # base case
        res = "1"
        
        # loop until we reach n
        for _ in range(n - 1):
            temp = ""
            cnt = 1
            
            for i in range(len(res)):
                # check if nxt char is same
                if i < len(res) - 1 and res[i] == res[i+1]:
                    cnt += 1
                else:
                    # hit a diff char or end. add to temp
                    temp += str(cnt) + res[i]
                    cnt = 1 # reset counter
            
            # update result for nxt round
            res = temp
            
        return res