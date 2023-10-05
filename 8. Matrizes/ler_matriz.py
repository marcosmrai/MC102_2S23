matriz = []

def transpose(matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    matriz_T = [[matriz[l][c] for l in range(n_linhas)] for c in range(n_colunas)]
    
    return matriz_T

def print_matriz(matriz):
    for linha in matriz:
        for i in linha:
            print("{0:5}".format(str(i)), end=' ')
        print()

def deepcopy(matrizes):
    if type(matrizes)==list:
        return [deepcopy(m) for m in matrizes]
    elif type(matrizes)==dict:
        return {deepcopy(m):deepcopy(matrizes[m]) for m in matrizes}
    else:#caso base
        return matrizes

def le_matriz():
    matriz=[]
    while True:
        linha_raw = input()
        if linha_raw == "":
            break
        linha_raw = linha_raw.strip().split()
        linha = [int(l) for l in linha_raw]
        matriz.append(linha)

    max_col = max([len(linha) for linha in matriz])

    matriz = [
            [linha[i] if i<len(linha) else None  for i in range(max_col)]
            for linha in matriz
            ]

    return matriz

def soma_matriz(matriz1, matriz2):
    n_linhas1 = len(matriz1)
    n_colunas1 = len(matriz1[0])
    
    n_linhas2 = len(matriz2)
    n_colunas2 = len(matriz2[0])

    if n_linhas1!=n_linhas2 or n_colunas1!=n_colunas2:
        print("Matrizes com numero de linhas e colunas diferentes.")
        return

    matriz = []

    for l in range(n_linhas1):
        linha = []
        for c in range(n_colunas2):
            if matriz1[l][c] is None or matriz2[l][c] is None:
                linha.append(None)
            else:
                linha.append(matriz1[l][c]+matriz2[l][c])
        matriz.append(linha)
    
    return matriz
            
def multiplica_matriz(matriz1, matriz2):
    n_linhas1 = len(matriz1)
    n_colunas1 = len(matriz1[0])
    
    n_linhas2 = len(matriz2)
    n_colunas2 = len(matriz2[0])

    if n_colunas1!=n_linhas2:
        print("Matrizes dimensões incompativeis.")
        return
    
    matriz = []
    for l in range(n_linhas1):
        linha = []
        for c in range(n_colunas2):
            valor = 0
            for i in range(n_colunas1):
                valor+=matriz1[l][i]*matriz2[i][c]
            linha.append(valor)
        matriz.append(linha)
    
    return matriz

def verifica_triang(matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])

    triang_sup = True
    triang_inf = True
    for l in range(n_linhas):
        for c in range(n_colunas):
            if c<l and matriz[l][c]!=0:
                triang_sup = False
            if c>l and matriz[l][c]!=0:
                triang_inf = False
    
    return triang_sup, triang_inf


matriz = le_matriz()
print(verifica_triang(matriz))