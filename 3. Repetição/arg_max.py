numeros = [-3, -1, -7, 9, -4]
maximo = -float("inf")
arg_max = None

for i, numero in enumerate(numeros):
    if numero > maximo:
        maximo = numero
        arg_max = i
    print(i, numero)

print("Maximo:", maximo)
print("Argumento do méximo:", arg_max)