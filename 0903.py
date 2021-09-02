n = int(input())
for i in range(n):
	st = input()
	print(st[0])

#joinの利用の仕方
#””（空白なしで）.joinする（以降の内容を）
#"+"にすれば、文字間に＋がはいって表示される
n = int(input())
st = [input() for i in range(n)]
result = "".join(i[0] for i in st)
print(result)