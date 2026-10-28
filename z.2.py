x = float(input("Podaj x"))
y = float(input("Podaj y"))
z = float(input("Podaj z"))
if x>y:
    x, y = y, x
if x>z:
    x,z = y, x
if x>z:
    x,z = z,x
print(f"Uporządkowane liczby {x}, {y}, {z}")

