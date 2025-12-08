import sys
N,K = map(int,sys.stdin.readline().split())
arr = []
cnt = 0
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.reverse()
for i in arr:
    cnt += K // i
    K%=i
print(cnt)