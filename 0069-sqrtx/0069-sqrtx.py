import math

class Solution:
    def mySqrt(self, x: int) -> int:
        self.x = x
        y = math.sqrt(self.x)
        y = math.floor(y)
        return y
