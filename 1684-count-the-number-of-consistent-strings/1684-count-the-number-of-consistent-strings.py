class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_set = set(allowed)
        consistency_counter = 0

        for word in words:
            consistency = True
            for char in word:
                if char not in allowed_set:
                    consistency = False
                    break
            if consistency:
                consistency_counter += 1

        return consistency_counter
        