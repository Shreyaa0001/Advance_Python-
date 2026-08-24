graph = {
    1: [(2, 15), (3, 20), (4, 10), (5, 35)],
    2: [(6, 25)],
    3: [(6, 30)],
    4: [(6, 20)],
    5: [(6, 15)],
    6: []
}

dp = {v: 999 for v in graph}
path = {}

dp[6] = 0

# Work backward
for u in [5, 4, 3, 2, 1]:
    for v, cost in graph[u]:
        if cost + dp[v] < dp[u]:
            dp[u] = cost + dp[v]
            path[u] = v

# Print result
print("Shortest Cost =", dp[1])

# Print path
u = 1
print("Shortest Path:", end=" ")

while u != 6:
    print(u, end=" -> ")
    u = path[u]

print(6)