import sys
cnt = int(sys.stdin.readline())
add = 0
a = sorted(map(int, sys.stdin.readline().split()))
b = sorted(map(int, sys.stdin.readline().split()))
b.reverse()
for i in range(cnt):
    add+=a[i]*b[i]
print(add)