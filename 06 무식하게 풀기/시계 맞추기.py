import sys
input = sys.stdin.readline

'''
4번 누르면 원상복귀되므로 10번 스위치까지 스위치당 0~3번 클릭

파이썬 시간초과 : 우선순위 만들기
(11,12,13번 시계는 연결된 스위치가 하나밖에 없으므로,
각각 연결된 1,4,9번 스위치 먼저 push()하며,
1,4,9번 스위치에서 11,12,13번 시계가 12시가 아니면 0번누르는 경우를 제외)
'''

switch = [
    [3,7,9,11],
    [6,7,8,10,12],
    [3,4,5,9,13],
    [0,4,5,6,7],
    [0,1,2],
    [1,2,3,4,5],
    [4,10,14,15],
    [0,2,14,15],
    [3,14,15],
    [4,5,7,14,15]
]

def click(s):
    for linked in switch[s]:
        clocks[linked] = (clocks[linked] + 3) % 12 or 12

minCount = float('inf')
def push(i, count):
    global minCount
    if minCount <= count:
        return
    if i == 10:
        if all(x == 12 for x in clocks):
            minCount = count
        return

    for cnt in range(4):
        if (i < 3) and clocks[i+11] != 12:
            click(i)
            continue
        push(i+1, count + cnt)
        click(i)


C = int(input())
for _ in range(C):

    clocks = list(map(int, input().split()))

    minCount = float('inf')
    push(0,0)
    print(minCount if minCount != float('inf') else -1)
