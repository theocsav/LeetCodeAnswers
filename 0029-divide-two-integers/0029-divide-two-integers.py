class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        negative = (dividend < 0) ^ (divisor < 0)
        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        for i in range(31, -1, -1):
            if (abs_divisor << i) <= abs_dividend:
                abs_dividend -= (abs_divisor << i)
                quotient += (1 << i)
        
        return -quotient if negative else quotient