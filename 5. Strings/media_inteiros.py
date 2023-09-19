inteiros = input("Digite numeros inteiros: ")
inteiros_split = inteiros.split()
eh_inteiro = [valor.isnumeric() for valor in inteiros_split]

if all(eh_inteiro):
    inteiros_inteiros = [int(valor) for valor in inteiros_split]
    print("A média é ", sum(inteiros_inteiros)/len(inteiros_inteiros) )
else:
    print("Digite de novo")
    