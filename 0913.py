print("1~9までの値を入力してください")
N=int(input())
A=[int(x) for x in input().split()]

count=[0]*9
for x in A:
	count[x-1] += 1

for i in count:
	print(i)

	N=int(input())
A=[int(x) for x in input().split()]

count=[0]*9
for x in A:
	count[x-1] += 1

max_n=count[0]
for y in count:
	if max_n < y:
		max_n = y
		
print(A[max_n])