agencia = input("Digite sua agência:")

lista = []
for digito in agencia:
    if digito.lower() == "x":
        lista.append(10)
    elif digito == "-":
        lista.append("-")
    else:
        lista.append(int(digito))


calculo_verif = 0
for i in range(0, 4):
    calculo_verif+=lista[i]*(5-i)

if 11 - calculo_verif%11 == lista[-1]:
    print("Agencia válida.")
else:
    print("Agencia inválida.")