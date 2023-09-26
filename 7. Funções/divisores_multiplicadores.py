def mmc(a, b):
    '''
    Função que calcula o minimo multiplicador comum de dois inteiros

            Parameters:
                    a (int): Um número inteiro
                    b (int): Um número inteiro

            Returns:
                    mmc(a, b): Retorna uma lista da fatoração em números primos
    '''
    if b is None:
        b = a
    lista_mmc = []
    primo = 2
    while a!=1 or b!=1:
        if a%primo==0 or b%primo==0:
            lista_mmc.append(primo)
            if a%primo==0:
                a = a//primo
            if b%primo==0:
                b = b//primo
        else:
            #vamos testar em numeros compostos, 
            #mas eles não vão conseguir dividir 
            #pois a e b já foram divididos pelos multiplicadores primos deles
            primo+=1
    return lista_mmc

def mdc(a, b):
    '''
    Função que calcula O máximo divisor comum de dois inteiros

            Parameters:
                    a (int): Um número inteiro
                    b (int): Um número inteiro

            Returns:
                    mdc(a, b): Retorna uma lista da fatoração em números primos
    '''
    lista_mdc = []
    primo = 2
    while a!=1 and b!=1:
        if a%primo==0 and b%primo==0:
            lista_mdc.append(primo)
            a = a//primo
            b = b//primo
        elif a%primo==0:
            a = a//primo
        elif b%primo==0:
            b = b//primo
        else:
            #vamos testar em numeros compostos, 
            #mas eles não vão conseguir dividir 
            #pois a e b já foram divididos pelos multiplicadores primos deles
            primo+=1
    return lista_mdc

def fatores_primos(a):
    return mdc(a, a)

numeros = []

while True:
    a = input("Digite um inteiro positivo: ")
    if a.isnumeric():
        a = int(a)
        numeros.append(a)
    else:
        break

def mult(lista):
    valor = 1
    for l in lista:
        valor*=l
    return valor

def mdc_varios(numeros):
    if len(numeros) == 1:
        return numeros[0]
    else:
        v1 = mdc_varios(numeros[len(numeros)//2:])
        v2 = mdc_varios(numeros[:len(numeros)//2])
        return mdc(v1, v2)

mdcs = mdc(numeros[0], numeros[1])
for numero in numeros[2:]:
    mdcs = mdc(mdcs, numero)





