atletas = ["João", "Fabio", "Marcelo", "Cleiton", "Cristiano"]
media_saltos = [12.3, 14.2, 10.1, 11.1, 13.5]

saltos_ordenados = sorted(media_saltos, reverse=True)

indice_maior_salto = media_saltos.index(saltos_ordenados[0])

for i, salto in enumerate(saltos_ordenados):
    idx = media_saltos.index(salto)
    print(i+1, "ésimo salto", salto, "é do", atletas[idx])