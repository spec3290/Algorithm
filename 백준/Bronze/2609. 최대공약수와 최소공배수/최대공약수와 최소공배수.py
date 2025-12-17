import math
import sys
a,b = map(int,sys.stdin.readline().split())
bg = math.gcd(a,b)
sm = math.lcm(a,b)
print(bg)
print(sm)