import sys
input = sys.stdin.readline
def isMatches(pattern, p, string, s):
    '''
    와일드카드 패턴 pattern[p:]과
    문자열 string[s:]이 대응하는 지 여부 판단
    '''
    global count, cache
    count += 1
    print(f'[{pattern[p:]}]-[{string[s:]}] 호출')

    if cache[p][s] != -1:
        return cache[p][s]

    if p < len(pattern) and s < len(string) and (pattern[p] == string[s] or pattern[p] == '?'):
        # 첫글자 매치 => 이후 글자에 대해 재귀호출
        cache[p][s] = isMatches(pattern, p + 1, string, s + 1)
        return cache[p][s]

    elif p == len(pattern):
        # 중간에 * 또는 매치 실패였다면 여기까지 안옴.
        # 패턴이 끝났으면 문자열도 끝나야만 매치
        cache[p][s] = (s == len(string))
        return cache[p][s]

    elif pattern[p] == '*':
        # 와일드카드를 만났다면
        # *이 아무런 문자에도 대응되지 않거나
        # *이 string의 1개 문자를 대응한다면 True
        # 재귀호출하기때문에 귀납적으로 1개문자 뿐만아니라 끝까지 검사하게됨
        if isMatches(pattern, p + 1, string, s) or \
                (s < len(string) and isMatches(pattern, p, string, s + 1)):
            cache[p][s] = 1
            return 1

    cache[p][s] = 0
    return 0


C = int(input())
for _ in range(C):
    W = input().rstrip()
    N = int(input())
    files = [input().rstrip() for _ in range(N)]

    count = 0
    ans = []
    for string in files:
        cache = [[-1 for _ in range(101)] for _ in range(101)]
        if isMatches(W, 0, string, 0):
            ans.append(string)

            print(f'>>>>>> {W}, {string} 매치 <<<<<<')
    print('\n'.join(sorted(ans)))
    print(f'총 호출 횟수 : {count}')
