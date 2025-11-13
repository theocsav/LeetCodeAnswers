class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                left_nodes = j - 1
                right_nodes = i - j


                dp[i] += dp[left_nodes] * dp[right_nodes]

        return dp[n]