class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp =  [[0] * m for i in range(n)]
        max_num = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    continue
                left = right = diag = 0
                if i > 0:
                    left = dp[i-1][j]
                if j > 0:
                    right = dp[i][j-1]
                if i > 0 and j > 0:
                    diag = dp[i-1][j-1]
                dp[i][j] = min([left, right, diag]) + 1
                max_num = max(max_num, dp[i][j])

        return max_num * max_num