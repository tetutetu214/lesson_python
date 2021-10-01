L,R=map(int,input(),split())

count=0

for x in range(L,R+1):

  S = str(x)
  flag = True
  N = len(S)
  for i in range(N):
    if S[i] != S[(N-1)-i]:
      flag = False
  if flag:
    count += 1

print(count)