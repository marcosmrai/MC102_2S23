x = int(input("Entre com um número inteiro positivo: "))
divisores = []
for i in range(1,x+1):
    if x%i==0:
        divisores.append(i)

print("Lista de {} divisores".format(len(divisores)))
print(divisores)
if divisores == [1, x]:
    print("O valor {} é primo.".format(x))