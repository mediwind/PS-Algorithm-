class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        while n >= k + 1:
            k += 1
            n -= k
        return k