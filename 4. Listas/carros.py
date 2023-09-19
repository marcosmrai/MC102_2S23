preco = 5.25
distancia = 1000
carros = []
consumos = []

while True:
    carro = input("Modelo do carro: ")
    if carro == "":
        break
    consumo = float(input("Consumo do carro: "))
    if carro in carros:
        idx = carros.index(carro)
        consumos[idx].append(consumo)
        consumo = None
    else:
        carros.append(carro)
        consumos.append([consumo])
    print()

print(carros)
print(consumos)

media_consumos = [sum(consumo)/len(consumo) for consumo in consumos]
melhor_consumo = max(media_consumos)
index_melhor_consumo = media_consumos.index(melhor_consumo)
print("O carro mais econômico é o", carros[index_melhor_consumo])


for i in range(len(carros)):
    print("O carro", carros[i], "vai gastar", distancia/media_consumos[i]*preco)

print(carros)
print(consumos)