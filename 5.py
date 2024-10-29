
# 5. Define a class that has at least two methods: getString: to get a string from the console
# input printString:
# to print the string in upper case. 
# Also, please include a simple test function to test the class methods.

class String:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter String: ")

    def printString(self):
        print(self.input_string.upper())


def stringconversion():
    str_conversion = String()
    str_conversion.getString()
    str_conversion.printString()



stringconversion()