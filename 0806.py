num = int(input())
for i in range(num):
  li = input().split()
  li.pop(0)
  for i in li:
    print(i)