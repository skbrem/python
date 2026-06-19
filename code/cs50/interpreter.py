expression = input("Expression: ")

x, y, z = expression.split(" ")

if y == "+":
    x = int(x)
    z = int(z)
    add = float(x + z)
    print(add)
elif y == "-":
    x = int(x)
    z = int(z)
    add = float(x - z)
    print(add)
elif y == "*":
    x = int(x)
    z = int(z)
    add = float(x * z)
    print(add)
elif y == "/":
    x = int(x)
    z = int(z)
    add = float(x / z)
    print(add)
