N=int(input())
A=[int(x) for x in input().split()]

#線形探索（集計）
count=[0]*9
for x in A:
	count[x-1] += 1


max_n=count[0]
for y in count:
	if max_n < y:
		max_n = y
		
print(A[max_n])


#解法
# データを受け取る
N = int(input())
A = list(map(int, input().split())) 

# 線形探索 (集計)
count = [0] * 9 
for x in A: 
    count[x-1] += 1

# 線形探索 (最大値)
index = 0
for i in range(9):
    if count[i] > count[index]: 
        index = i

# 答えを出力する
ans = index + 1
print(ans)

N = int(input())
A = [int(x) for x in input().split()]

max_n = 0
for i in range(N):
	if A[i] > A[max_n]:
		max_n = i
print(max_n)

