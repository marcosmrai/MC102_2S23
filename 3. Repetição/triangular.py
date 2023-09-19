N = int(input("Digite um número: "))

triangular = False

i = 1
while (i*(i+1)*(i+2)) > N:
    if (i*(i+1)*(i+2))==N:
        print(N, "é um numero triangular divisível por", i, i+1, i+2)
        #triangular = True
        break
    i += 1
else:
    print("Não é triangular.")
#if not triangular:
#    print("Não é triangular.")