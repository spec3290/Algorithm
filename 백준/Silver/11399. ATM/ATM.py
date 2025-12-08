import sys
n = int(sys.stdin.readline())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()
prev = 0
answer = 0
for i in range(n):
    prev = prev+my_list[i]
    answer += prev
print(answer)