n = int(input())

# fib1 실행 횟수 = 피보나치 수
f = [0] * (n + 1)
f[1] = 1
if n >= 2:
    f[2] = 1

for i in range(3, n + 1):
    f[i] = f[i-1] + f[i-2]

# fib2 실행 횟수 = n - 2
print(f[n], n - 2)

