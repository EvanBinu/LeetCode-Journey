class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if i==j:
                    s+=mat[i][j]
                elif j == n-i-1:
                    s+=mat[i][j]
        
        return s