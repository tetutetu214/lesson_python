N, K=map(int,input().split())

count = 0
add = 0

for i in range(1,N+1):
    for x in range(1,i):
        #print(x)
        #print(i)
        #if i % x == 0: 
        #  count += 1
        print(i % x)
    #print(count)
    
    #if count == K:

    #    add += 1
#print(add)

N, K = map(int, input().split())

# 数字の全探索
count = 0
for x in range(1, N+1):
    # 約数の個数を求める (数字の全探索)
    yaku = 0
    for i in range(1, x+1):
        if x%i == 0: 
            yaku += 1
    # 約数の個数が $K$ 個ならば 1 を足す
    if yaku == K: 
        count += 1

# 答えを出力する
print(count)

N,K =map(int,input().split())
count=0
for x in range(1,N+1):
  add=0
  for i in range(1,x+1):
      if x % i == 0:
          add += 1
      
      if add == K:
          count += 1

print(count) 