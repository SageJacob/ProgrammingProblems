import sys


def contiguous(arr):
    ans = -sys.maxsize
    a = 0
    for i in range(len(arr)):
        a += arr[i]
        ans = max(ans, a)
        a = max(a, 0)
    return ans
