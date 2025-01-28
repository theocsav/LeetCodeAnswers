class Solution:
    def climbStairs(self, n: int, cache=None) -> int:
        if cache is None:
            cache = {}

        if n in cache:
            return cache[n]

        if n <= 2:
            return n
        
        cache[n] = self.climbStairs(n - 1, cache) + self.climbStairs(n - 2, cache)

        return cache[n]