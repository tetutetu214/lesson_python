def helloWorld():
  return "Hello World!"

def add(num1, num2):
  add = num1 + num2
  return add

#Pythonの配列[](){}をつかうよ
#リスト：なかの値を変えることが出来る
list = ["a","b","c"]
print(list)
print(list[0])

#タプル：なかの値を変えることが出来ない
#基本形
tuple = ("a", 5 , 3.14)
print(tuple)
print(tuple[0])
#応用
def third(tuple):
  return (tuple[2]) 

#ディクショナリ：
#基本形
dict = {"key": "value","key2": "value2"}
print(dict)
print(dict["key2"]) →"valu2"が出力される
#応用
def create_dict(key, value):
  return {key: value}


def calc_total(nums):
  add = 0
  for i in nums:
    add += i
  return add