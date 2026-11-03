# 0/1 Knapsack using Top-Down and Bottom-Up DP

# Top-Down Approach (Memoization)
def knapsack_top_down(weights, values, capacity, n, memo):
    if n == 0 or capacity == 0:
        return 0

    if memo[n][capacity] != -1:
        return memo[n][capacity]

    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack_top_down(
            weights, values, capacity, n - 1, memo
        )
    else:
        include = values[n - 1] + knapsack_top_down(
            weights, values, capacity - weights[n - 1], n - 1, memo
        )
        exclude = knapsack_top_down(
            weights, values, capacity, n - 1, memo
        )
        memo[n][capacity] = max(include, exclude)

    return memo[n][capacity]


# Bottom-Up Approach (Tabulation)
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Main Program
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

n = len(weights)

memo = [[-1 for _ in range(capacity + 1)]
        for _ in range(n + 1)]

top_down_result = knapsack_top_down(
    weights, values, capacity, n, memo
)

bottom_up_result = knapsack_bottom_up(
    weights, values, capacity
)

print("Top-Down DP Maximum Value:", top_down_result)
print("Bottom-Up DP Maximum Value:", bottom_up_result)