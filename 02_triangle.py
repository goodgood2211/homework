# 2. 写程序用while实现打印三角形。
#   要求输入一个整数表示三角形的宽度和高度,打印出如下的三种直角三角形
#   1)
#       *
#      **
#     ***
#    ****
#   2)
#    ****
#     ***
#      **
#       *
#   3) 
#    ****
#    ***
#    **
#    *

w = int(input("请输入三角形的宽度: "))
i = 1  # i代表星号的个数和行数
while i <= w:
    blanks_count = w - i  # 空格数=宽度-星号个数
    print(' ' * blanks_count + '*' * i)
    i += 1

print('------第二个三角形------')
i = w  # i代表星号的个数
while i > 0:
    blanks_count = w - i # 计算空格数
    print(' ' * blanks_count + '*' * i)
    i -= 1  # 让星号变少

print('------第三个三角形------')
i = w  # i代表星号的个数
while i > 0:
    print('*' * i)
    i -= 1