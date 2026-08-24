cost = [0,10,20,30]
memo={}
def travel(n):
    if n in memo:
        return memo[n]
    if n ==0:
        return 0
    if n == 1:
        return cost[1]      
    memo[n] = min(travel(n-1)+cost[1], travel(n-2))
    return memo[n]
print(travel(3))