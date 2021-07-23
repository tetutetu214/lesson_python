import random

print ("1〜5までの数値を入れてね、占うよ")
get = int(input())
omikuzi = random.randint(1,5)

if get <= 5:
  if  omikuzi == get:
    print("なんということだ")
  elif omikuzi == 2:
    print("激レア")
  else:
    print("そうでもない")
else:
  print ("1~5までの数値を入れてねって言ったよね？")
print ("なんだと")