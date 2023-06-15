# 练习:
#   输入一个整数n, 判断这个整数是否是素数(prime)
#     (素数是指只能被1 和自身整除的数)
#     如:
#       2 3 5 7 11...
#     方法：
#       用排除法.一但n能被2~n-1的数整除就不是素
#        数，否则就一定是素数

n = int(input("请输入一个整数: "))

if n < 2:
    print(n, '不是素数')
    exit()

# 方法 1
# flag = True  # true代表是素数，False代表不是素数
# for i in range(2, n):
#     if n % i == 0:
#         # print(n, '不是素数!')
#         flag = False
#         break
# if flag == True:
#     print(n, '是素数!')
# else:
#     print(n, '不是素数!')

# 方法2:
for i in range(2, n):
    if n % i == 0:
        print(n, '不是素数!')
        break
else:
    print(n, '是素数!')

