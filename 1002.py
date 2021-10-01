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