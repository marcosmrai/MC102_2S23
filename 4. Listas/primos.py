N = int(input("Digite um inteiro: "))

primos = []

for i in range(2, N+1):
    for divisor in primos:
        if i%divisor==0:
            break
    else:
        primos.append(i)

print(primos)