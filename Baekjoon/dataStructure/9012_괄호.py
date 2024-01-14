n = int(input())
stack=[]

# 1번 생각 : 스택에 (를 넣고 )일때 pop해서 짝을 맞춰서 넣게끔 구현
# but stack empty 때문에 예외처리해줌
# 근데 틀림
'''
for i in range (n):
    for j in blank[i] :
        if j == "(" :
            stack.append(j)
        elif j == ")" :
            try :
                stack.pop()
            except:
                break
    if stack is [] :
        print("YES")
    else:
        print("NO")
'''
# 정답
# break로 끊기지 않고 수행됐을 경우에는 if가 아니라 else로 시작했어야함!! 그래서 틀림
# 그리고 굳이 처음에 한번에 리스트로 받을 필요 없이 바로바로 검증하는게 효율적
for i in range (n):
    stack=[]
    blank = input()

    for j in blank :
        if j == "(" :
            stack.append(j)
        elif j == ")" :
            if stack :
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack :
            print("YES")
        else:
            print("NO")