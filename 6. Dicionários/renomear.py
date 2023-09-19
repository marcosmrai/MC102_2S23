dicio = {'nome':"João das Couves", 10:"Eita nois", 1.20:"float"}
dicio['interjeicao'] = dicio.pop(10)

idades = {"Maria": 31, "Marcelo":40, "Enzo":10}

valores_idades = list(idades.values())
chaves_idades = list(idades.keys())
min_idade = min(list(idades.values()))
idx = valores_idades.index(min_idade)

#print(chaves_idades[idx])

#print(sorted(idades, key= lambda chave: idades[chave]))

print(sorted(idades))

sorted_dict = {nome:idades[nome] for nome in sorted(idades)}
sorted_dict2 = {nome:idades[nome] for nome in sorted(idades, key= lambda chave: idades[chave])}

print(sorted_dict2)


## Pokehuman

idades = {"Maria": {'Tipo':'Fogo', 'Idade':31}, "Marcelo": {'Tipo':'Agua', 'Idade':57}, "Enzo":  {'Tipo':'Fogo', 'Idade':42},}

valores_idades = [idades[nome]['Idade'] if idades[nome]['Tipo'] == 'Fogo' else -float('inf') for nome in idades]
print(valores_idades)

chaves_idades = list(idades.keys())
min_idade = max(list(valores_idades))
idx = valores_idades.index(min_idade)

print(chaves_idades[idx])

import numpy as np

print(np.array([2, 3, 5])@np.array([4, 3, 1]))