#入れ替えをする
s = input()
a, b = [int(x) for x in input().split()]
s_list = list(s)
tmp = s_list[a-1]
s_list[a-1] = s_list[b-1]
s_list[b-1] = tmp
s = "".join(s_list)
print(s)

#sum関数を利用する
n = int(input())
num = [int(x) for x in input().split()]
print(sum(num))

#関数を利用せずforで繰り返す
n = int(input())
num = [int(x) for x in input().split()]
#print(sum(num))
add = 0
for i in num:
  add += i
print(add)

#関数を利用せずforで繰り返す
n = input()
num = [int(x) for x in input().split()]
mul = 1
for i in num:
	mul *= i
print(mul)

#1桁目を表示する
n = int(input())
num = [int(x) for x in input().split()]
for i in num:
	print(i%10)

#リストの値が3で割り切れるなら表示する
n = int(input())
num = [int(x) for x in input().split()]
for i in num:
	div = i % 3
	if div == 0:
		print(i)