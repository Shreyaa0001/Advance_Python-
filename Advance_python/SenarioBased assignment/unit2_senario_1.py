# Fibonacci Sequence using Memoization (Top-Down DP)
memo = {}

def fibonacci(n):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]

N = int(input("Enter the number of Fibonacci numbers: "))

sequence = []

for i in range(N):
    sequence.append(fibonacci(i))

print("Fibonacci Sequence:")
print(sequence)