import sys
while(True):
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    elif arr[0] * arr[0] + arr[1] * arr[1] == arr[2] * arr[2]:
        print("right")
    else:
        print("wrong")
