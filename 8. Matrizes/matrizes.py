l = int(input("Entre com o número de linhas: "))
c = int(input("Entre com o número de colunas: "))
matriz = []

def deepcopy(matrizes):
    if type(matrizes)==list:
        return [deepcopy(m) for m in matrizes]
    elif type(matrizes)==dict:
        return {deepcopy(m):deepcopy(matrizes[m]) for m in matrizes}
    else:#caso base
        return matrizes
    
    

for i in range(l):
    linha = []
    for j in range(c):  
        linha.append(i*c+j+1) # recebendo os dados
    matriz.append(linha)

matriz_cp = deepcopy(matriz)

matriz_cp[0][1] = 10000

print(matriz)