import sys
input = sys.stdin.readline

def JLIS(idxA, idxB):
    if cache[idxA+1][idxB+1]:
        return cache[idxA+1][idxB+1]
    # print(f'call JLIS({idxA},{idxB})', end=' | ')
    a = -float('inf') if idxA == -1 else A[idxA]
    b = -float('inf') if idxB == -1 else B[idxB]
    maxElement = max(a, b)
    # print(f'{a} vs {b} - maxE = {maxElement}')

    res = 2
    for nextA in range(idxA+1, len(A)):
        if A[nextA] > maxElement:
            res = max(res, JLIS(nextA, idxB) + 1)

    for nextB in range(idxB+1, len(B)):
        if B[nextB] > maxElement:
            res = max(res, JLIS(idxA, nextB) + 1)

    cache[idxA+1][idxB+1] = res
    # print(f'JLIS({idxA},{idxB})에서 res = {res}')
    return res


C = int(input())
for _ in range(C):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cache = [[0 for _ in range(M+1)] for _ in range(N+1)]

    print(JLIS(-1, -1) - 2)