import sys

N = int(sys.stdin.readline())

d = [0] * (N+1)   # dp 테이블 - i를 1로 만드는 데 필요한 최소 연산 횟수 저장

for i in range(2, N+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)


print(d[N])

# d[2] = min(d[2], d[1]+1) = 1
# d[3] = min(2,1) = 1







# 10 -> 9 -> 3 -> 1   : 3번
# 16 -> 8 -> 4 -> 2 -> 1  : 4번
# 17 -> 16 -> 8 -> 4 -> 2 -> 1 : 5번
# 56 -> 28 -> 27 -> 9 -> 3 -> 1 : 5번
# 40 -> 20 -> 10 -> 9 -> 3 -> 1 : 5번



