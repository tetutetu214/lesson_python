N=int(input())
A=[int(x) for x in input().split()]

count = 0
add = 0

for i in A:
  if i < 2:
    count += 1
  elif i == 2:
    count += 1
  else:
    for x in range(2,i-1):
      if i % x == 0:
        add += 1
    if add < 1:
      count +=1
print(count)