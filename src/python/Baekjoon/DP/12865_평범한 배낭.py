import sys
input = sys.stdin.readline

n, k = map(int, input().split())
item = []

for i in range (n):
    w, v = map(int, input().split())
    item.append((w, v))

dp = [0 for _ in range(k+1)]

for i in item:
    w, v = i
    for j in range(k, w-1, -1):
        #합이 k 이하인 dp안에 저장된 가치와 현재 가치를 더한 값과 현재 가치를 비교후 최댓값 출력
        dp[j] = max(dp[j], dp[j-w]+v)


print(dp[-1])