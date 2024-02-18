
def tiling(n):
    '''
    2 X N 타일을 채우는 방법
    = 맨 왼쪽 2X1을 세로 1개로 채우고 2X(N-1)을 채우는 방법
        + 맨 왼쪽 2X2를 가로 2개로 채우고 2X(N-2)를 채우는 방법
    '''
    global MOD
    if n <= 2:
        return n
    dp = [0 for _ in range(n+1)]
    dp[1], dp[2] = 1, 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    return dp[n] % MOD

MOD = 1000000007
C = int(input())
for _ in range(C):
    N = int(input())
    print(tiling(N))