numeros = [-3, -1, -7, -9, -4]
maximo = -float("inf")
i = 0

while i < len(numeros):
    if numeros[i] > maximo:
        maximo = numeros[i]
    i = i + 1
print(maximo)