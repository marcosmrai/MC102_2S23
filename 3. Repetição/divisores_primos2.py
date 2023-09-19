valor = int(input("Entre com um número inteiro positivo: "))
divisores = []

while valor>1:
    for divisor in range(2, valor+1):
        if valor%divisor==0:
            divisores.append(divisor)
            valor = valor//divisor
            break
            
        
print(divisores)