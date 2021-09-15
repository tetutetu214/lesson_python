A, B = map(int, input().split()) 

ans = 0
for i in range(1,max(A,B)+1) :
    if A % i == 0 and B % i == 0:
        ans = i
print(ans)

