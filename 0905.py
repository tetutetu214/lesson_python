n = int(input())
st = [input() for i in range(n)]
le = st.count('left')
ri = st.count('right')
if le > ri:
  print('left')
elif le < ri:
  print('right')
else:
  print('same')




a,b = map(int, input().split())
num = [int(x) for x in input().split()]
if b in num:
    print("Yes")
else:
    print("No")