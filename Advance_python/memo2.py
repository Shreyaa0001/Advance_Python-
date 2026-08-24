def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(5))
print(fib(10))
print(fib(20))

print("=====================")
n = 4
table = [0] * (n+1)
table[0]=0
table[1]=1
for i in range(2, n+1):
    table[i] = table[i-1] + table [i-2]
print(table)
print("Ficonacci of 4 = ",table[4])    