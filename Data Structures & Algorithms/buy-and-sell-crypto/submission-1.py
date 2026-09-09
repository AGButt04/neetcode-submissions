class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = math.inf
        maxProfit = 0

        for p in prices:
            if buy > p:
                buy = p
            else:
                maxProfit = max(maxProfit, p - buy)
        
        return maxProfit