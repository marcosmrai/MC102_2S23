def contador(lista):
    dicio = {}
    for l in lista:
        if l not in dicio:
            dicio[l] = 1
        else:
            dicio[l] += 1
    
    return dicio

def conjunto(lista):
    dicio = contador(lista)
    return list(dicio.keys())

def moda(lista):
    dicio = contador(lista)
    max_value = max(dicio.values())
    maiores = []
    for key, value in dicio.items():
        if value==max_value:
            maiores.append(key)
    return maiores

def uniao(lista1, lista2):
    conj1 = conjunto(lista1)
    conj2 = conjunto(lista2)
    return conjunto(conj1+conj2)

def interseccao(lista1, lista2):
    conj1 = conjunto(lista1)
    conj2 = conjunto(lista2)
    return [c1 for c1 in conj1 if c1 in conj2]

def diferenca(lista1, lista2):
    conj1 = conjunto(lista1)
    conj2 = conjunto(lista2)
    return [c1 for c1 in conj1 if c1 not in conj2]


lista1 = [10, 9, 12, 13, 9, 12, 10, 8, 10 , 9]
lista2 = [13, 17, 9, 8, 5, 1, 2]

print(diferenca(lista1, lista2))
