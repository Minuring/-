import sys
input = sys.stdin.readline

def jump(i, j):
    global memo
    if i >= N or j >= N:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]
    if i == N-1 and j == N-1:
        return 1

    memo[i][j] = 0
    if jump(i+board[i][j], j) or jump(i, j+board[i][j]):
        memo[i][j] = 1

    return memo[i][j]


C = int(input())
for _ in range(C):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    memo = [[-1 for _ in range(N)] for _ in range(N)]

    print('YES' if jump(0,0) else 'NO')