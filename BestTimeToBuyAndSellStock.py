class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        mprof = 0

        for right in range(1,len(prices)):
            if  prices[right] < prices[left]:
                left = right
            else:
                mprof = max(mprof, prices[right]-prices [left])
        return mprof

# I dont understand why this is a sliding window problem. 
