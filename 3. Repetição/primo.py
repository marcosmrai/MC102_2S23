x = int(input("Entre com um número inteiro positivo: "))
divisores = []
for i in range(1,x+1):
    if x%i==0:
        break
else:
    print("Primo.")