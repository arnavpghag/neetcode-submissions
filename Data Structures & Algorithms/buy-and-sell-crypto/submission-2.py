class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        least=prices[0]
        for i in prices:
            if i<least:
                least=i
            if profit< i-least:
                profit=i-least
        return profit
            