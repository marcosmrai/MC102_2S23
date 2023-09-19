n = int(input("Entre com um número inteiro positivo: "))
divisores = []
for valor in range(n+1):
    if valor>1:
        # como eu tenho todos os primos de 2 a valor-1 na lista divisores
        # então eu posso só testar os divisores primos na lista divisores
        for divisor in divisores:
            if valor%divisor==0:
                break
        else:
            divisores.append(valor)
    #na lista divisores eu tenho todos os primos de 2 a valor
print(divisores)