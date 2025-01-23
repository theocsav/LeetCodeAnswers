class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0

        guess = x

        while True:
            new_guess = (guess + x / guess) / 2
            if abs(guess - new_guess) < 1e-6:
                break
            guess = new_guess

        return int(guess)
