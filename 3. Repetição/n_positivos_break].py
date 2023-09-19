n = 0
while True:
    x = int(input("Entre com um número inteiro positivo: "))
    if x > 0:
        n = n + 1
    else:
        break
    print("Invariante", n)

print("Quantidade de números positivos fornecidos:", n)