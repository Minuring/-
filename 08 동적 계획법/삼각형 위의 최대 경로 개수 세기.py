import sys
input = sys.stdin.readline

def count(i, j):
    global maxScore
    # T[i][j]에서 최대경로의 개수
    # = T[i+1][j]에서 최대경로 개수 + T[i+1][j+1]에서 최대경로 개수
    # S[i][j] = i, j에서 맨 밑까지 내려갔을 때 얻을 수 있는 최대점수
    # 최대 경로의개수는 S[i+1][j], S[i+1][j+1] 중 큰 곳으로 가야만 함
    if i == N-1:
        return 1

    if cache[i][j] is not None:
        return cache[i][j]

    result = 0
    if S[i+1][j] > S[i+1][j+1]:
        result = count(i+1, j)
    elif S[i+1][j] < S[i+1][j+1]:
        result = count(i+1, j+1)
    else:
        result = count(i+1, j) + count(i+1, j+1)

    cache[i][j] = result
    return cache[i][j]



def score():
    dp = [[0 for j in range(i)] for i in range(1, N+1)]

    dp[-1] = T[-1]
    for i in range(N-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + T[i][j]

    return dp


C = int(input())
for _ in range(C):
    N = int(input())
    T = [list(map(int, input().split())) for _ in range(N)]

    S = score()
    cache = [[None for j in range(i)] for i in range(1, N+1)]

    print(count(0,0))