S=input()
S_len=len(S)
count=0
for i in S:
	add=0
	for x in range(S_len):
		if i == S[x]:
			add += 1
			if add < 2:
				count += 1
print(count)

# データを受け取る
S = input()
N = len(S)

# 文字の全探索
count = 0
for x in range(ord('a'), ord('z')+1):
    c = chr(x)
    # S に c が含まれるかを調べる
    flag = False
    for i in range(N):
        if S[i] == c:
            flag = True
    # S に c が含まれるならば 1 を足す
    if flag:
        count += 1

# 答えを出力する
print(count)