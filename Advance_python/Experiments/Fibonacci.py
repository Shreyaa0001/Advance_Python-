def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1
  
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
  
n = int(input("Enter the value of n: "))

print("The", n, "th Fibonacci number is:", fibonacci(n))

#Output
#Enter the value of n: 10
#The 10 th Fibonacci number is: 55
