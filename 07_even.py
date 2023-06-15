# 练习:
#   输入一个整数用begin绑定，再输入一个整数用end绑定，打印出从begin~end(包含end)的所有偶数
#     (建议用continue语句跳过奇数)

begin = int(input("请输入一个开始整数: "))
end = int(input("请输入一个结束整数: "))

for x in range(begin, end):
    if x % 2 == 1:
        continue
    print(x)
