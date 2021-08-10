def fizzbuzz(n):
  if n % 15 == 0:
    return("FizzBuzz")
  elif n % 3 == 0:
    return("Fizz")
  elif n % 5 == 0:
    return("Buzz")    
  else:  
    return str(n) 

list = [1, 2, 3]
list.append(5)
print(list)

#リストの中に”5”はいくつありますか？
list = [1, 5, 3, 5, 6]
list.append(5)
num = list.count(5)
print(num)

#リストから取り出して削除する
list = [1, 5, 3, 5, 6]
list.append(5)
#該当する値をリストの中で後ろから検索して削除
#この場合appendで5をリストの最後に入れるも、popで消しているのでリストの状態が出力
num = list.pop(5)
print(num)

#リストの中に存在しているかを例外処理で書いてみる
list = [1, 5, 3, 5, 6]
list.append(5)
#この場合1度目でリストの中に5がありますか？あるので5が出力
#2度目はリストの中にないので例外処理のexceptの文章が出力
try:
  print(list.index(5))
  print(list.index(4))
except NameError:
  print("リストにはないよ")
