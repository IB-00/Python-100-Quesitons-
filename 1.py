# 1. Write a program that will find all such numbers divisible by 7 but not a multiple of 5, between
# 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# divisible by 7 but not a mulitple of 5
# 2000 and 3200 is the range

list = []

for num in range(2000,3201):
    if num %7 == 0 and num % 5 != 0:
        list.append(num)
print("number divisible by 7 but not a multiple of 5:", list)








