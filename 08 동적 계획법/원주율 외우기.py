import sys
input = sys.stdin.readline
from collections import Counter

# 시간초과
# def score(N, idx, digit):
#     dif = N[idx+1] - N[idx]
#     if all(x == N[idx] for x in N[idx:idx + digit]):
#         return 1
#     elif all(N[x] + 1 == N[x + 1] for x in range(idx, idx + digit - 1)) \
#             or all(N[x] == N[x - 1] - 1 for x in range(idx + digit - 1, idx, -1)):
#         return 2
#     elif len(Counter(N[idx:idx + digit])) == 2:
#         return 4
#     elif all(N[x + 1] - N[x] == dif for x in range(idx, idx + digit - 1)):
#         return 5
#     return 10

def score(a, b, c, d=None, e=None):
    if a==b==c and (a==d if d is not None else True) and (a==e if e is not None else True):
        return 1
    elif (a-b==b-c==1 or a-b==b-c==-1) and (a-b==c-d if d is not None else True) and (a-b==d-e if e is not None else True):
        return 2
    elif (d is None and a==c != b) or (d is not None and e is None and a==c and b==d and b!=c) or (e is not None and a==c==e and b==d and a!=b):
        return 4
    elif a-b == b-c and (a-b == c-d if d is not None else True) and (a-b == d-e if e is not None else True):
        return 5

    return 10

def difficult(N):
    maxLen = len(N)

    cache = [None] * (maxLen+1)
    for digit in range(3, 6):
        cache[digit] = score(*N[:digit])

    for i in range(6, maxLen+1):
        candidates = []
        for d in range(3, 6):
            if cache[i-d] is not None:
                candidates.append(cache[i-d] + score(*N[i-d:i]))
        # print(f'{i}에서 cand = {candidates}')
        cache[i] = min(candidates)
    return cache[-1]

C = int(input())
for _ in range(C):
    N = list(map(int, input().rstrip()))
    print(difficult(N))