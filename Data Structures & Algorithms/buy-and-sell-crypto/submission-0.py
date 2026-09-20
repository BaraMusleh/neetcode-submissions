class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxPrice = 0
        profit = 0
        
        for price in prices:
            if price < minPrice : 
                minPrice = price

            currentProfit = price - minPrice

            if profit < currentProfit : 
                profit = currentProfit

        return profit