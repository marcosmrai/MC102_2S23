dicio = {'nome':"João das Couves", 10:"Eita nois", 1.20:"float"}

dicio["nome"] = "Maria Joaquina"

if "nome" in dicio:
    print(dicio['nome'])
if "universidade" in dicio:
    print(dicio['universidade'])
else:
    print("universidade não está em dicio")

value = dicio.get("nome")
if value is not None:
    print(value)

print(dicio.items())
#operações de remoção
'''
print(len(dicio))

print("POP:", dicio.pop("nome"))

del dicio[10]

print(dicio)

print(dicio.popitem())
'''
## inicio da digressão sobre is
## is dá True quando as variaveis apontam para o mesmo endereço
value1 = []
value2 = []
value2 = value1

if value1 is value2:
    print("OK")

## Fim da digressão sobre is


localizacao = dict ({
'nome': "Centro Campinas",
"lat": -22.817087 ,
"lon": -47.069760})

localizacao2 = dict ({
"nome": "Barão Geraldo",
"lat": -23.877087 ,
"lon": -47.169750})

lista = [localizacao, localizacao2]

print("{2:30} {0:10} {1:10}".format("Latitude", "Longitude", "Localização"))


for l in lista:
    print("{2:30} {0:10.4f} {1:10.4f}".format(l['lat'], l['lon'], l['nome']))

'''
dicio_entrada = {}
while True:
    nome = input("Digite um nome: ")
    if nome == '':
        break
    idade = int(input("Digite uma idade: "))
    dicio_entrada[nome] = idade

print(dicio_entrada)

teste = {"idades":[18]}
teste['idades'].append(125)

print(teste)
'''

dic = {
"A": "Abacate",
"B": "Banana",
"C": "Caqui"
}

for key in dic:
    print(key, dic[key])

print()

for key, item in dic.items():
    print(key, item)

print(dic.items())

dicionario_complicado = {'lista':[1, 2, 3], 'nome':"Marcos"}
dicionario_complicado2 = dicionario_complicado.copy()

dicionario_complicado2['nome'] = "Maria"
dicionario_complicado2['lista'][1] = 100
print(dicionario_complicado)

print()

pessoas = ["Alice", "Beatriz", "Carlos"]
telefones = ["99999-0000", "99999-1111", "99999-2222"]
enderecos = ["rua 5", 'rua 10', 'rua 3']

for tupla in zip(pessoas, telefones, enderecos):
    print(tupla)

print()

dicionario = dict(zip(pessoas, telefones))
print(dicionario)

print()

dicionario_bla = {}
for n, t, e in zip(pessoas, telefones, enderecos):
    dicionario_bla[n] = {'telefone':t, 'endereço':e}

print(dicionario_bla)