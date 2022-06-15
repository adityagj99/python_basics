#String concatenation programe

def min_to_sec():
    m = int(input("Minutes: "))

    s = m*60

    return print("Seconds: " + str(s))
    print(f"Seconds are: {s}")  #f -> format
    print(f"second: {m* 60}")

min_to_sec()