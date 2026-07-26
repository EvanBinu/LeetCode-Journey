class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        for r in range(n):
            for c in range(n):
                num = matrix[r][c]
                if num in rows[r] or num in cols[c]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
        return True