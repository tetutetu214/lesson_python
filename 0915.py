N=int(input())
A=[int(x) for x in input().split()]

count = [0]*9
for x in A:
	count[x-1] += 1

index = 0
for i in range(9):
	if count[i] > count[index]:
		index=i
ans = index + 1
print(ans)