num = [int(x) for x in input().split()]
print(sum(num))

num = [int(x) for x in input().split()]
print(max(num))

num = [int(x) for x in input().split() ]
one = num[0] % 10
two = num[1] % 10
if one > two:
  print(num[1])
else:
  print(num[0])

num = [int(x) for x in input().split()]
if num[0] % num[1] == 0:
  print("Yes")
else:
  print("No")

num = [int(x) for x in input().split()]
print(int(sum(num)/len(num)))