class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s_list[left] not in vowels:
                left+= 1
            elif s_list[right] not in vowels:
                right -= 1
            else:
                temp = s_list[right]
                s_list[right] = s_list[left]
                s_list[left] = temp
                left += 1
                right -= 1
        
        return ''.join(s_list)