valor_buscado = 20
lista = [2, 4, 7, 1, 0, 8, 9, 5]
for valor in lista:
    print(valor)
    if valor == valor_buscado:
        print("Valor encontrado:", valor)
        break
else:
    print("Valor não encontrado.")