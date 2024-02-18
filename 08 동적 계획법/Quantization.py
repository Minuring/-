import sys
input = sys.stdin.readline
from itertools import accumulate

def minError(start, size):
    import decimal
    '''
    A[start:start+size+1] 의 평균 = 양자화 값 O(size)
    오차 제곱의 합 = (A[s]-m)^2 + (A[s+1]-m)^2 + ... + (A[s+size]-m)^2
        = sum(A[i]^2) - 2*sum(A[i])*m + m^2 * size
    '''
    hi = start + size - 1
    partSum_pow = acc_powA[hi] - (acc_powA[start - 1] if start > 0 else 0)
    partSum = accA[hi] - (accA[start - 1] if start > 0 else 0)
    # QValue = int((partSum + 0.5) / size)
    QValue = int('{:.0f}'.format(partSum / size))
    error = partSum_pow - (2 * QValue * partSum) + ((QValue ** 2) * size)
    # print(f'minError({start},{size}) : partSum={partSum}, QV={QValue}, error={error}')
    return error

def quantize(start, parts):
    '''
    A[start:]을 parts개 묶음(숫자)로 양자화해서 얻을 수 있는 최소 오차(제곱의 합)

    = minError(start, start+size-1) + quantize(start+size, parts-1)
    minError : A[start : start+size] 를 한 묶음으로 양자화 했을 때 최소 오차
    1 <= size <= len(A) - start
    '''
    global N, S
    if start == N:
        return 0
    if parts == 0:
        return float('inf')
    if cache[start][parts-1] != -1:
        return cache[start][parts-1]

    result = float('inf')
    for size in range(1, N - start + 1):
        error = minError(start, size) + quantize(start+size, parts-1)
        # print(f'A[{start}]부터 {size}개 양자화 후 최소 오차제곱합 = {error}')
        result = min(result, error)

    cache[start][parts-1] = result
    return result

C = int(input())
for _ in range(C):
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    accA = list(accumulate(A))
    acc_powA = list(accumulate([x**2 for x in A]))
    cache = [[-1 for _ in range(S)] for _ in range(N)]

    print(quantize(0, S))