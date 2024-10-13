class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        while i < len(chars):
            char = chars[i]
            count = 0
            
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            chars[j] = char
            j += 1
            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1
        return j
            