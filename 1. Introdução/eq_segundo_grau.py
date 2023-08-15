a = 0
b = 2
c = 8

if a!=0:
    delta = (b**2)-(4*a*c)
    if delta >= 0:
        x1 = (-b+delta**(1/2))/(2*a)
        x2 = (-b-delta**(1/2))/(2*a)
        print(x1, x2)
    else:
        print("Delta é negativo")
else:
    x = -c/b
    print("Raiz única:", x)