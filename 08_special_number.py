# 练习:
#   求 1 ~ 100(包含100) 之间所有不能
#   被5,7,11整除的数的和是多少?
#     (建议用continue语句实现)

s = 0  # 用来保存累加和

# 方法1
# for x in range(1, 101):
#     if x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
#         continue
#     s += x

# 方法2
for x in range(1, 101):
    if x % 5 == 0:
        continue
    if x % 7 == 0:
        continue
    if x % 11 == 0:
        continue
    s += x

print("和是: ", s)
