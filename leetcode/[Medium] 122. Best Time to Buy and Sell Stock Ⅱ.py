class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock, profit = 0, 0
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > stock:
                stock = prices[i]
            elif prices[i] < stock:
                profit += stock - prices[i]
                stock = prices[i]
        return profit