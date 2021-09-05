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