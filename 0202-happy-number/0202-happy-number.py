class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            s = 0
            while n:
                s += (n%10)**2
                n = n//10
            return s
        d = set()
        while True:
            if n==1:
                return True
            if n in d:
                return False
            d.add(n)
            n = sumOfSquares(n)