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


#数字全探索
N = int(input())

count = 0

for i in range(1,N+1):
  if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
      count += 1
print(count)

N=int(input())

count = 0
for i in range(1,N+1):
  if N % i == 0:
    count += 1
print(count)

N = int(input())

count = 0
for i in range(1,N+1):
	if N % i == 0:
		count += 1

if count == 2:
	print("Yes")
else:
	print("No")