#https://www.acmicpc.net/problem/12738

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
d = []
cnt = 0
d.append(a[0])

def lower_bound(arr,n,key):
    left = 0
    right = n

    while right > left:
        mid = (right+left)//2
        if arr[mid] >= key:
            right = mid
        else:
            left = mid + 1

    return right

for i in range(1,n):
    if a[i] > d[cnt]:
        d.append(a[i])
        cnt += 1
    else:
        p = lower_bound(d,cnt,a[i])
        d[p] = a[i]
print(len(d))


"""
def lower_bound(x):
    i = 0
    j = len(ans) - 1

    while i <= j:
        mid = (i+j) // 2
        if d[mid] == x:
            j = mid - 1
        elif d[mid] > x:
            j = mid - 1
        else:
            i = mid + 1

    return i
"""