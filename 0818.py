num = int(input())
for i in range(num):
  name = input().split()
  age = int(name[1]) + 1
  print(name[0],age)

a = int(input())
b = int(input())
print(a * b)

#複数の文字列を受け取り整数としてリスト

num = [int(x) for x in input().split()]
print(sum(num))

num = [int(x) for x in input().split()]
print(max(num))

a, b = map(int, input().split())
if a > b:
	print a
	else:
	print b