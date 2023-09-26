def soma(valores):
    s = 0
    for v in valores:
        s+=v

    return s

def minimo(valores):
    m = float('inf')
    for v in valores:
        if v<m:
            m = v

    return m

#maximo de valores reais
def maximo(valores):
    m = -float('inf')
    for v in valores:
        if v>m:
            m = v

    return m

def encontra(valores, valor):
    for i, v in enumerate(valores):
        if v==valor:
            return i
    return None

def encontra_substring(valores, valor):
    for i, v in enumerate(valores):
        if valor in v:
            return i
    return None

def multiplica_soma(listas):
    def somador(l):
        soma = 0
        for v in lista:
            soma+=v
        return soma
    
    mult = 1
    for lista in listas:
        soma = somador(lista)
        mult*=soma

    return mult

def funcao(a, b, c, d=1, e=4, f=10):
    print(e-d)

def incrementa_argumento(x):
    x = x+1
    if x==0:
        return
    print(x)

def main():
    variavel = "Olá"
    print("sdkljadklaskjdhnaskmah")
    #retorno = incrementa_argumento(x)
    #print(retorno)
    teste()

def teste():
    print()

if __name__ == '__main__':
    main()

print("sdkljadklaskjdhnaskmah")