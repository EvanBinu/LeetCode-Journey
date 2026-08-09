class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        rest = 0
        sold = 0
        for i in range(len(prices)):
            prevhold = hold
            prevrest = rest
            prevsold = sold
            hold = max(prevhold,prevrest - prices[i])
            sold = prevhold+prices[i]
            rest = max(prevrest,prevsold)
        return max(sold,rest)