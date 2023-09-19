tuplas = [(1, ), (1, 4, 2), (2, 1), (1, ), (3, 2, 5), (2, 4, 1, 65)]

dim = max([len(tupla) for tupla in tuplas])
medianas = []

for d in range(dim):
    lista = [tupla[d] for tupla in tuplas if len(tupla)>d]
    lista.sort()
    medio = len(lista)//2
    if len(lista)%2 == 0:
        mediana = (lista[medio]+lista[medio-1])/2
    else:
        mediana = lista[medio]
    medianas.append(mediana)

medianas = tuple(medianas)

print(medianas)