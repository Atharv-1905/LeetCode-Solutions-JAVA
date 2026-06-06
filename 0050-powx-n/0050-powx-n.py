class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.myPow(x, -n)
            
        half_pow = self.myPow(x, n // 2)

        if n % 2 == 0:
            return half_pow * half_pow
        # If n is odd, we square the half-power and multiply by one more x
        else:
            return half_pow * half_pow * x