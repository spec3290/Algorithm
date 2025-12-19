import sys
import math
a,b,v = list(map(int,sys.stdin.readline().split()))
rh = v-a
j = a-b
day = 1

print(math.ceil(rh/(j)) + day)