# 练习:
#   任意输入一个字符串，判断这个字符串中有几个空格' '
#   (要求不允许用S.count方法)
#   建议使用for语句实现

s = input("请输入一段字符串: ")

count = 0  # 此变量用来记录空格的个数
for ch in s:
    # 如果ch绑定空格，则将count 做 加1操作
    if ch == ' ':
        count += 1

print("空格的个数是:", count)