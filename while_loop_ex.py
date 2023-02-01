# 1-2-23
# print any 5 variable using while loop
num = 0
while num <= 10:
    num += 1
    if num % 2 != 0:
        continue
    print(num)