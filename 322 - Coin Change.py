class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        return dp[amount] if dp[amount] < float('inf') else -1