class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # maxi = 0
        for l in range(len(prices)):
            for r in range(l+1,len(prices)):
                if prices[r]>prices[l]:
                    profit = max(profit, prices[r]-prices[l])
                
                if prices[r]>prices[l]:
                    maxi = 1
                    
        return profit                   
        #     maxi = max(maxi, prices[l])
        # if maxi !=0 :
        #     return profit
        
        # else:
        #     return 0
