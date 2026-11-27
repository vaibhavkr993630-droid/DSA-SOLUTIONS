
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            factor, price = items[i]
            bonus = free[i]

            prev = dp[:]
            curr = dp[:]

            for b in range(price, budget + 1):
                curr[b] = max(
                    prev[b],
                    curr[b - price] + 1,
                    prev[b - price] + 1 + bonus
                )

            dp = curr

        return dp[budget]
