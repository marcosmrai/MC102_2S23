Ps = [[7.0, 8.3, 10.0, 6.5, 9.3], [8.5, 6.9, 5.0, 7.5, 9.8], [9.9, 9.1, 8]]

medias = []
for i, prova in enumerate(Ps): 
    medias.append(sum(prova)/len(prova))
    print("Media da P"+str(i+1)+":", medias[i])

nota_max = max(medias)

maior_index = medias.index(nota_max)

print("P"+str(maior_index+1)+" teve maior média.")