import numpy as np

a = np.random.choice([3, 6, 7])

def imprime_tabuleiro(tabuleiro):
    for i in range(13):
        print('_', end='')
    print()
    for i in range(3):
        print('|', end='')
        for j in range(3):
            print(tabuleiro[i][j]['valor'] if tabuleiro[i][j]['valor'] is not None else " ", end='') 
        print('|', end='')
        for j in range(3, 6):
            print(tabuleiro[i][j]['valor'] if tabuleiro[i][j]['valor'] is not None else " ", end='')
        print('|', end='')
        for j in range(6, 9):
            print(tabuleiro[i][j]['valor'] if tabuleiro[i][j]['valor'] is not None else " ", end='')
        print('|')
    
    for i in range(13):
        print('_', end='')
    print()

    for i in range(3, 6):
        print('|', end='')
        for j in range(3):
            print(tabuleiro[i][j]['valor'] if tabuleiro[i][j]['valor'] is not None else " ", end='')
        print('|', end='')
        for j in range(3, 6):
            print(tabuleiro[i][j]['valor'] if tabuleiro[i][j]['valor'] is not None else " ", end='')
        print('|', end='')
        for j in range(6, 9):
            print(tabuleiro[i][j]['valor'] if tabuleiro[i][j]['valor'] is not None else " ", end='')
        print('|')
    
    for i in range(13):
        print('_', end='')
    print()

    for i in range(6, 9):
        print('|', end='')
        for j in range(3):
            print(tabuleiro[i][j]['valor'] if tabuleiro[i][j]['valor'] is not None else " ", end='')
        print('|', end='')
        for j in range(3, 6):
            print(tabuleiro[i][j]['valor'] if tabuleiro[i][j]['valor'] is not None else " ", end='')
        print('|', end='')
        for j in range(6, 9):
            print(tabuleiro[i][j]['valor'] if tabuleiro[i][j]['valor'] is not None else " ", end='')
        print('|')
    
    for i in range(13):
        print('_', end='')
    print()
        

def cria_tabuleiro_vazio():
    tabuleiro = []
    for linha in range(9):
        linha_tabuleiro = []
        for coluna in range(9):
            celula = {'linha':linha,
                    'coluna':coluna,
                    'itens_possiveis':set(range(9)),
                    'valor':None}
            
            mesma_linha = [(linha, i) for i in range(9)]
            mesma_coluna = [(i, coluna) for i in range(9)]
            quadrante_coluna = coluna//3
            quadrante_linha = linha//3
            mesma_quadrante = [(quadrante_linha*3+i, quadrante_coluna*3+j) for i in range(3) for j in range(3)]

            celula['vizinhos'] = mesma_linha+mesma_coluna+mesma_quadrante
            celula['vizinhos'] = set(celula['vizinhos'])

            linha_tabuleiro.append(celula)
        tabuleiro.append(linha_tabuleiro)
    return tabuleiro

def resolve_tabuleiro(tabuleiro):
    menos_opcoes = None
    opcoes = float('inf')

    for linha in np.random.permutation(9):
        for coluna in np.random.permutation(9):
            if opcoes > len(tabuleiro[linha][coluna]['itens_possiveis']) and tabuleiro[linha][coluna]['valor'] is None:
                opcoes = len(tabuleiro[linha][coluna]['itens_possiveis'])
                menos_opcoes = (linha, coluna)

    (linha, coluna) = menos_opcoes
    valor_escolhido = np.random.choice(list(tabuleiro[linha][coluna]['itens_possiveis']))
    for (i, j) in tabuleiro[linha][coluna]['vizinhos']:
        if valor_escolhido in tabuleiro[i][j]['itens_possiveis']:
            tabuleiro[i][j]['itens_possiveis'].remove(valor_escolhido)

    tabuleiro[linha][coluna]['itens_possiveis'] = [valor_escolhido]
    tabuleiro[linha][coluna]['valor'] = valor_escolhido

tabuleiro = cria_tabuleiro_vazio()
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)

resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
resolve_tabuleiro(tabuleiro)
imprime_tabuleiro(tabuleiro)