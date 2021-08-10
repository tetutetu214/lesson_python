def compare(val1, val2):
  if val1 == val2:
    return 0
  elif val1 > val2:
    return 1
  else:
    return -1

def multiple_total(a, b):
  i = 0
  total = 0
  while i <= b:
    if i % a == 0:
      total += i
    i += 1
  return total