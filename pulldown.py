#HTMLで表示させてみるプルダウン方法

print("<select name=\'age\'>")

for i in range(10):
  print("<option>" + str(i+1) + "才</option>")

print("</select>")