a = float(input("Enter 1st Number: "))
o = input("Enter Opearator: ")
b = float(input("Enter 2nd Number: "))

if(o == "+"):
    ans = a+b

if (o == "-"):
    ans = a-b

if (o == "*"):
    ans = a*b

if (o == "/"):
    ans = a/b

print(f"{a} {o} {b} = {ans}")