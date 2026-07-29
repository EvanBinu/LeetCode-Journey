class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = 0
        left = k - 1
        right = len(cardPoints) - 1
        for i in range(left+1):
            s+=cardPoints[i]
        ms = max(s,0)
        while left > -1:
            s+= cardPoints[right] - cardPoints[left]
            left-=1
            right-=1
            ms = max(ms,s)
        return ms