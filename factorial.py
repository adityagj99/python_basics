#factorial

num = int(input("Enter Number: "))

def factorial(n):
    if n<0:
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        fact = 1
        while(n>0):
            fact = n*fact
            n -= 1
        return fact

print(factorial(num))