class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        low=prices[0]
        for index, less in enumerate(prices):
            if low>less:
                low=less
                continue
            if profit<less-low:
                profit=less-low

        return profit