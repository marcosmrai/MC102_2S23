tuplas = [(1, ), (1, 4, 2), (2, 1), (1, ), (3, 2, 5), (2, 4, 1, 65)]

novas_tuplas = [tupla for tupla in tuplas if len(tupla)>=3]
primeiro_elemento = [tupla[0] for tupla in tuplas]

terceiro_elemento = [tupla[2] if len(tupla)>=3 else None for tupla in tuplas ]

print(terceiro_elemento)