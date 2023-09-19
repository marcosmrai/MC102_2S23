lista = [1, 12.1, 7, 8.5, 9.1, 5, 2.3]
lista.sort()
medio = len(lista)//2
if len(lista)%2 == 0:
    mediana = (lista[medio]+lista[medio-1])/2
else:
    mediana = lista[medio]

print(mediana)