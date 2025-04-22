class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left, right = 0, 1
        # profit = 0
        # while right < len(prices):
        #     isValley = prices[left] > prices[right]
        #     isPeak = right == len(prices)-1 or prices[right] > prices[right+1]
        #     if isValley:
        #         left = right
        #     if isPeak:
        #         profit += prices[right] - prices[left]
        #         left = right
        #     right += 1
        profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]

        return profit