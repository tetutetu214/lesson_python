def compare(val1, val2):
  if val1 == val2:
    return 0
  elif val1 > val2:
    return 1
  else:
    return -1

#引数aの倍数のうち、引数b以下のものの合計値を算出するメソッド
def multiple_total(a, b):
  i = 0
  total = 0
  while i <= b:
#aの倍数とは即ち、自身で割って余りが0になるものを指す
    if i % a == 0:
      total += i
    i += 1
  return total