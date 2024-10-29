
# 4. Write a program that accepts a sequence of comma-separated numbers from the
# console and generates a list and a tuple that contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')


numbers = input("Enter Numbers to assing in list and Tuple: ")
my_list = []
data = numbers.split(',')
for number in data:
    my_list.append(number.strip())                   
my_tuple = tuple(my_list)                   
print(my_list)
print(my_tuple)