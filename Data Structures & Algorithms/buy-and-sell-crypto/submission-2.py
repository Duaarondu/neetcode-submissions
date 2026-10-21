class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        low = float("inf")
        for price in prices:
            low = min(low,price)
            best = max(best,price-low)
        return best