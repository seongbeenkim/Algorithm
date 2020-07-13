#https://www.acmicpc.net/problem/1149

import sys

n = int(sys.stdin.readline())
house = []
d = [[0] * 3 for _ in range(n)]

for _ in range(n):
    i = list(map(int,sys.stdin.readline().split()))
    house.append(i)

d[0][0] = house[0][0]
d[0][1] = house[0][1]
d[0][2] = house[0][2]

for i in range(1,n):
    d[i][0] = min(d[i-1][1],d[i-1][2]) + house[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + house[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + house[i][2]

print(min(d[n-1]))