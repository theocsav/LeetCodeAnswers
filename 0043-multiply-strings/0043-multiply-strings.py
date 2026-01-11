class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # if either number is 0, the answer is just 0
        if num1 == "0" or num2 == "0":
            return "0"
        
        # the result length can be at most len1 + len2
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        # loop backwards just like doing math on paper
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                
                # correct position in the result array
                p1 = i + j
                p2 = i + j + 1
                
                # add the multiplication result to whats already there
                total = mul + res[p2]
                
                # set the current spot and carry over the rest
                res[p2] = total % 10
                res[p1] += total // 10
        
        # turn the array back into a string
        # skip leading zeros if any exist
        result_str = "".join(map(str, res))
        
        return result_str.lstrip("0") if result_str.lstrip("0") else "0"