base = int(input("Entre com a base: "))
expoente = int(input("Entre com o expoente: "))

if expoente<0:
    base = 1/base
    expoente = -expoente

resultado = 1
i = 0
while i < expoente:
    resultado = resultado*base
    i += 1

print("Resultado:", resultado)