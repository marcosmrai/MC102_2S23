nomes_atletas = []
saltos_atletas = []

while True:
    nome_atleta = input("Nome do atleta: ")
    if nome_atleta == "":
        break
    nomes_atletas.append(nome_atleta)
    saltos_atleta = []
    for i in range(5):
        salto_atleta = float(input("Distância do salto:"))
        saltos_atleta.append(salto_atleta)
    media = 0
    for salto in saltos_atleta:
        media+=salto
    media/=5
    saltos_atletas.append(media)


for i in range(len(nomes_atletas)):
    print("Nome do atleta:", nomes_atletas[i])
    print("Média dos saltos do atleta:", saltos_atletas[i])