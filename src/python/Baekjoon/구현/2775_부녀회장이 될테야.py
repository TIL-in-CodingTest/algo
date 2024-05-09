case = int(input())
arr = []

def house(k, n):
    # 0층의 거주민 초기화
    arr = [i for i in range(1, n + 1)]

    for i in range(k):
        for j in range(1, n):
            # 현재 층의 j호까지의 거주민 수를 계산하여 저장
            arr[j] += arr[j - 1]

    return arr[n - 1]

for _ in range (case):
    k = int(input())
    n = int(input())
    
    result = house(k, n)
    print(result)