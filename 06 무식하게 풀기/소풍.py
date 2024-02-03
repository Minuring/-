import sys
input = sys.stdin.readline

'''
아직 짝을 찾지 못 한 학생 중 >>번호가 낮은 학생부터<< 매칭
중복 카운트 방지를 위해 순서 강제


'''
def pair(paired):
    global N, friend, ans
    if all(paired):
        ans += 1
        return

    student = paired.index(False)
    for other in range(student + 1, N):
        if friend[student][other] and not paired[student] and not paired[other]:

            paired[student] = paired[other] = True
            pair(paired)
            paired[student] = paired[other] = False


C = int(input())
for _ in range(C):
    ans = 0
    N, M = map(int, input().split())
    pairs = list(map(int, input().split()))
    friend = [[False for _ in range(N)] for _ in range(N)]
    for i in range(0, M*2, 2):
        a, b = pairs[i], pairs[i+1]
        friend[a][b] = friend[b][a] = True

    pair([False for _ in range(N)])
    print(ans)