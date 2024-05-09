i = 0
while True:
    i+=1 # 순서
    l, p, v = map(int, input().split())
    if l==0 and p==0 and v==0: # 0 0 0 나올때까지 입력받기
        break
    a = v//p
    b = v%p
    if l<b:
        b = l
    print("Case %d: %d" %(i, a*l+b))