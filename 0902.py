#入れ替えをする
s = input()
a, b = [int(x) for x in input().split()]
s_list = list(s)
tmp = s_list[a-1]
s_list[a-1] = s_list[b-1]
s_list[b-1] = tmp
s = "".join(s_list)
print(s)