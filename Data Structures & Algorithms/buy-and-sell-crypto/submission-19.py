class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
            
        while r < len(prices):
            
            if prices[l] > prices[r]:
                l = r
            
            
            p = prices[r] - prices[l]
            
            max_profit = max(p, max_profit)
            print("l: ", l)
            print("R: ", r)
            print("cur profit: ", p)
            print("max profit: ", max_profit)
            r += 1
        return max_profit
