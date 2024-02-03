import sys
input = sys.stdin.readline

'''
보드에서 남은 흰색 칸 중 >>가장 왼쪽 위<<의 칸에 블럭을 덮어본다.
왼쪽 혹은 위쪽을 이미 채웠다고 가정하기 때문에 블럭 모양은 아래 혹은 오른쪽으로
(중복 계산을 방지하기 위한 순서 강제)

가장 왼쪽 위의 흰색칸을 찾고, (흰색칸이 없으면 성공- 리턴)
오른쪽, 혹은 밑으로만 채우는 블럭을 덮어보고, 재귀호출 후 다시 걷어낸다.
'''

WHITE, BLACK = '.', '#'
deltas = [
    [(0,0), (0,1), (1,0)],
    [(0,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1)],
    [(0,0), (1,0), (1,-1)]
]
def findFirst():
    for i in range(H):
        for j in range(W):
            if board[i][j] == WHITE:
                return i, j
    return -1, -1
def check(y, x, shape):
    for dy, dx in shape:
        ny, nx = y+dy, x+dx
        if not (0 <= ny < H and 0 <= nx < W and board[ny][nx] == WHITE):
            return False
    return True

def cover_or_discover(y, x, shape, discover=False):
    for dy, dx in shape:
        ny, nx = y+dy, x+dx
        board[ny][nx] = BLACK if not discover else WHITE
def cover():
    y, x = findFirst()
    if y == -1 and x == -1:
        return 1

    count = 0
    for shape in deltas:
        if check(y, x, shape):
            cover_or_discover(y, x, shape, discover=False)
            count += cover()
            cover_or_discover(y, x, shape, discover=True)

    return count

C = int(input())
for _ in range(C):
    H, W = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(H)]

    print(cover())
