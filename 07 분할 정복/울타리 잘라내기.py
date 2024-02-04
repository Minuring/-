import sys
input = sys.stdin.readline

def bruteForce(fence, left, right): # O(N^2)
    # l번 판자~ r번 판자까지 : min(fence[l~r]) * (r - l + 1)
    ans = 0
    for l in range(left, right + 1):
        minH = fence[l]
        for r in range(l, right + 1):
            minH = min(minH, fence[r])
            ans = max(ans, minH * (r - l + 1))

    return ans

def bruteForce_Enhanced(fence, left, right): # O(N)
    mid = (left + right) // 2
    lo, hi = mid, mid + 1
    height = min(fence[lo], fence[hi])
    maxArea = height * 2
    while lo > left or hi < right:
        if hi < right and (lo == left or fence[lo-1] < fence[hi+1]):
            # hi가 범위 내에 있고,
            # lo가 범위 밖이거나 hi쪽 확장이 더 클 때
            height = min(height, fence[hi+1])
            hi += 1
        else:
            height = min(height, fence[lo-1])
            lo -= 1

        maxArea = max(maxArea, height * (hi - lo + 1))
    return maxArea

def solve(fence, left, right):
    if left == right:
        return fence[left]

    mid = (left + right) // 2
    maxArea = max(solve(fence, left, mid), solve(fence, mid+1, right))
    maxArea = max(maxArea, bruteForce_Enhanced(fence, left, right))

    return maxArea

C = int(input())
for _ in range(C):
    N = int(input())
    fence = list(map(int, input().split()))
    #print(bruteForce(fence, 0, N-1)) # 완탐

    print(solve(fence, 0, N-1))
