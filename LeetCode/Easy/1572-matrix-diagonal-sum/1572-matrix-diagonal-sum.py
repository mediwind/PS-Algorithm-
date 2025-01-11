class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n - 1 - i]
        
        if n % 2:
            ans -= mat[n // 2][n // 2]
        
        return ans