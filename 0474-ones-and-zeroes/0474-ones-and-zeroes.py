class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            c0 = s.count('0')
            c1 = s.count('1')
            for z in range(m,c0-1,-1):
                for c in range(n,c1-1,-1):
                    dp[z][c] = max(dp[z][c],1+dp[z-c0][c-c1])
        return dp[m][n]