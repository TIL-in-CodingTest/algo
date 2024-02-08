import sys
from collections import Counter
n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]
array.sort()

print(round(sum(array)/n))
print(array[n//2])

cnt = Counter(array).most_common()
if len(cnt) >1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else :
    print(cnt[0][0])

print(max(array)-min(array))