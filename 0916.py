A, B = map(int, input().split()) 

ans = 0
for i in range(1,max(A,B)+1) :
    if A % i == 0 and B % i == 0:
        ans = i
print(ans)

N = int(input())

for i in range(1,N+1):
  if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
  elif i % 3 == 0:
      print("Fizz")
  elif i % 5 == 0:
      print("Buzz")
  else:
      print(i)

S = input()
c = input()
N = len(S)

flag = False
for i in range(N):
  if S[i] == c:
      flag = True

if flag:print("Yes")
else:print("No")

S = input()
N = len(S)
A = S[::-1]

flag = False
for i in range(N):
	if S[i] == A[i]:
		flag = True
	else:
		flag = False

if flag:print("Yes")
else:print("No")

#上記を改良したバージョン
S = input()
N = len(S)
A = S[::-1]

flag = True
for i in range(N):
	if S[i] != A[i]:
		flag = False

if flag:print("Yes")
else:print("No")