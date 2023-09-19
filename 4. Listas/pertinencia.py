lista = []
while True:
    valor = int(input("Insira um valor positivo: "))
    if valor>0:
        lista.append(valor)
    else:
        break
x = int(input("Qual o número a procurar? "))
if x in lista:
    print(x, "pertence à lista e está na posição", lista.index(x))
else:
    print(x, "não pertence à lista")