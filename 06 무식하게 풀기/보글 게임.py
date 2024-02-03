import sys
input = sys.stdin.readline

'''
find() : 칸 i, j에서 target 글자를 만들 수 있는 지 여부를 리턴
target[:] == target[0] + target[1:]

첫글자 틀리면 False.
elif 첫글자 하나면 True
else 주변 8칸에서 target[1:]을 만들 수 있으면 True

남은 글자 수, i, j 혹은 i, j에서의 8방향 으로 메모이제이션
'''

deltaY, deltaX = [-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]
def find(i, j, target):
    global cache
    #i, j에서 주어진 단어가 시작하는 지
    if not (0 <= i < 5 and 0 <= j < 5):
        return False
    if board[i][j] != target[0]:
        return False
    if len(target) == 1:
        return True
    if cache[len(target)-1][i][j] != 0:
        return cache[len(target)-1][i][j]

    cache[len(target)-1][i][j] = -1
    for dy, dx in zip(deltaY, deltaX):
        ny, nx = i + dy, j + dx
        if find(ny, nx, target[1:]) == 1:
            cache[len(target)-1][i][j] = 1
            break

    return cache[len(target)-1][i][j]

C = int(input())
for _ in range(C):
    board = [list(input().rstrip()) for _ in range(5)]
    N = int(input())
    for _ in range(N):
        target = input().rstrip()

        flag = False
        for i in range(5):
            for j in range(5):
                cache = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(10)]
                if find(i, j, target) == 1:
                    flag = True
                    break

            if flag: break

        print(target, "YES" if flag else "NO", sep=' ')