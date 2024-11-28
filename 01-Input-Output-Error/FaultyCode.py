# print("Hello World) #Jutumärgid lõpetamata

# print("Hello World") #Taande viga

# if __name__ == '__main__':
#  print("hello World") # puuduv taane viga

# print(underclared_variable + 10) # --> NameError / var is not defined

variable = "viis"
print(variable + 10)  # TypeError: can only concatenate str (not "int") to str
print(10 + variable)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'


def third(a):
    print(int(a))  # Attempt to convert string <The output is called 'Stack Trace'> to int and print it out


def second(a, b):
    c = a + b
    print(c)  # --> The output is called 'Stack Trace'

    # Calling the third function
    third(c)


def first():
    # Calling the second function
    second("The output is called ", "'Stack Trace'")


first()
