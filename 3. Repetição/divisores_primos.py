n = int(input("Entre com um número inteiro positivo: "))
divisores = []
# neste "criamos" valor para ver se ele é primo
for valor in range(n+1):
    if valor>1:
        # como eu tenho todos os primos de 2 a valor-1 na lista divisores
        # então eu posso só testar os divisores primos na lista divisores
        # neste for, testamos se valor é primo
        for divisor in divisores:
            if valor%divisor==0:
                break
        else:
            divisores.append(valor)
    #na lista divisores eu tenho todos os primos de 2 a valor

divisores_primos = []
for divisor in divisores:
    if n%divisor==0:
        divisores_primos.append(divisor)

print(divisores_primos)