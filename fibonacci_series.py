# Fibonacci Series

print("Fibonacci Series \n")
a = int(input("Enter requried numbers: "))

def fibonacci_series():
    print(" ")
    f1 = 0
    f2 = 1
    if a == 0:
        return "Invalid input"
    elif a == 1:
        return 0
    n = [f1,f2]
    for i in range(a-2):
        result = f1 + f2
        f1 = f2
        f2 = result
        n.append(result)
    return n
print(f"\nFibonacci Series upto {a} is:")
print(fibonacci_series())