class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        length = min(len(word1), len(word2))

        for i in range(length):
            result.append(word1[i])
            result.append(word2[i])
        
        result.append(word1[length:])
        result.append(word2[length:])

        return "".join(result)