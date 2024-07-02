class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print("Output:", solution.maxProfit(prices)) 
prices = [7, 6, 4, 3, 1]
print("Output:", solution.maxProfit(prices))