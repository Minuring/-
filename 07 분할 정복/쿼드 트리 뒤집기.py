import sys
input = sys.stdin.readline
'''
압축해제 decompress()는 실제 사용하지 않고 ( 용량이 너무 큼. 불가능 )
압축 해제하지 않고 바로 상하로 뒤집기

재귀적으로 압축과 동일한 방법으로 4사분면으로 나눠서 뒤집기
'''

MAX_SIZE = 2 ** 4
BLACK, WHITE = 'b', 'w'
def decompress(string, i, j, size):
    '''
    1. i = [0, len(tree)/2) j = [0, len(tree)/2)
    2. i = [0, len(tree)/2), j = [len(tree)/2, len(tree))
    3. i = [len(tree)/2, len(tree)), j = [0, len(tree)/2)
    4. i = [len(tree)/2, len(tree)), j = [len(tree)/2, len(tree)]
    '''

    global it
    if it == len(string):
        return

    prefix = string[it]
    it += 1

    if prefix == BLACK or prefix == WHITE:
        # i~i+size, j~j+size = prefix
        for y in range(i, i + size):
            for x in range(j, j + size):
                decompressed[y][x] = prefix
    else:
        mid = size // 2
        decompress(string, i, j, mid)
        decompress(string, i, j + mid, mid)
        decompress(string, i + mid, j, mid)
        decompress(string, i + mid, j + mid, mid)


def reverse(string):
    global it
    if it == len(string):
        return ''

    prefix = string[it]
    it += 1

    if prefix == BLACK or prefix == WHITE:
        return prefix

    upperLeft = reverse(string)
    upperRight = reverse(string)
    lowerLeft = reverse(string)
    lowerRight = reverse(string)

    return 'x' + lowerLeft + lowerRight + upperLeft + upperRight


C = int(input())
for _ in range(C):
    compressedString = list(input().rstrip())

    it = 0
    decompressed = [['' for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]
    decompress(compressedString, 0, 0, MAX_SIZE)

    for row in decompressed:
        print(*row)

    it = 0
    print(reverse(compressedString))