N = int(input("Digite um inteiro: "))

primos = []

for i in range(2, N+1):
    for divisor in primos:
        if i%divisor==0:
            break
    else:
        primos.append(i)

goldbach = True

for x in range(4, N+1):
    if x%2==1:
        continue
    for primo_i in primos:
        if x-primo_i in primos:
            #print(x, "=", primo_i, "+", x-primo_i)
            break
    else:
        goldbach = False

print("Goldbach é", goldbach)