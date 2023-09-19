idades = []
alturas = []

N = int(input("Numero de alunos"))

for i in range(N):
    idade = int(input("Idade:"))
    altura = float(input("Altura:"))
    idades.append(idade)
    alturas.append(altura)

media = 0
for altura in alturas:
    media+=altura
media/=N

total_alunos = 0
for i in range(N):
    if idades[i]>13 and alturas[i]<media:
        total_alunos +=1

print("Total de alunos:", total_alunos)