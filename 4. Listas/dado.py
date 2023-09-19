import random

N = int(input("Numero de rodadas de dado."))

rolagens = []

for i in range(N):
    dado = random.randint(1, 6)
    rolagens.append(dado)

for outcome in range(1, 7):
    print(outcome, "saiu", rolagens.count(outcome))