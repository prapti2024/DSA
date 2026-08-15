
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0 

        for coin in coins:
            
            for current in range(coin, amount+1):
                
                dp[current] = min(dp[current],dp[current-coin]+1)

        if dp[amount]<100000:
            return dp[amount]
        else:
          return -1 
        