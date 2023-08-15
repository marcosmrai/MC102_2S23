a = -1
b = float("inf")
c = float("inf")

if a>=b and a>=c:
    maior = a
    if b>c:
        meio = b
        menor = c
    else:
        meio = c
        menor = b
elif b>=a and b>=c:
    maior = b
    if a>c:
        meio = a
        menor = c
    else:
        meio = c
        menor = a
else:
    maior = c
    if a>b:
        meio = a
        menor = b
    else:
        meio = b
        menor = a

print(menor, meio, maior)