
def add():
    print("\nAddition")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(" ")
    result = print(f"{num1} + {num2} = {num1+num2} \n")
    return result

def sub():
    print("\nSubtraction")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(" ")
    result = print(f"{num1} - {num2} = {num1-num2} \n")
    return result

def mul():
    print("\nMultilication")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(" ")
    result = print(f"{num1} * {num2} = \n{num1*num2} \n")
    return result

def div():
    print("\nDivision")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(" ")
    result = print(f"{num1} / {num2} = \n{num1/num2} \n")


user_input = ""
while user_input != "exit()": 
    print(f"Calculator \n")
    print(f'''
    Press '1' for Addition \n
    Press '2' for Subtraction \n
    Press '3' for Multiplication \n
    Press '4' for Division \n
    Type 'exit()' to Quit
    ''')

    user_input = (input("Enter your choice: "))

    if user_input == "exit()":
        print("\nThank you for using me!")
        break
    else:
        if user_input == '1':
            add()
        elif user_input == '2':
            sub()
        elif user_input == '3':
            mul()
        elif user_input == '4':
            div()
        else:
            print("\nSelect Valid Option \n")