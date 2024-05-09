#첫번째 집을 각각 RGB로 칠했다고 가정한 후에 
#이전 집을 다른 두 색 중에 비용의 최솟값으로 더함
#배열 중 가장 작은 값 선택하면 그것이 비용의 최솟값

n = int(input())

RGB = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    RGB[i][0] += min(RGB[i-1][1], RGB[i-1][2])  #R
    RGB[i][1] += min(RGB[i-1][0], RGB[i-1][2])  #G
    RGB[i][2] += min(RGB[i-1][0], RGB[i-1][1])  #B
    
print(min((RGB[n-1])))