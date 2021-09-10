N = int(input())
A = [int(x) for x in input().split()]
count = 0
for i in range(1,N):
  if A[i-1] < A[i]:
    count += 1
print(count)


N = int(input())
A = [int(x) for x in input().split()]
maxnum = A[0]
for i in A:
  if i > maxnum:
    maxnum = i
print(maxnum)

# データを受け取る
N = int(input()) 
A = list(map(int, input().split())) 

# 線形探索
index = 0 
for i in range(N): 
    if A[i] > A[index]:  
        index = i 

# 答えを出力する
print(index) 