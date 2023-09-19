import getpass

while True:
    erros = 0
    palavra = getpass.getpass("Digite a palavra:").lower()
    if palavra == "":
        print('Que pena, venha jogar de novo')
        break
    palavra_aux = list(palavra)
    palavra_revelada = ['_' for l in palavra]
    while erros < 6:
        letra = input("Digite uma letra: ")
        if len(letra)>1:
            if letra == palavra:
                print('Ganhou')
                break
            else:
                continue

        if letra.lower() not in palavra:
            print("ERRRROU")
            erros += 1
        
        while letra.lower() in palavra_aux:
            idx = palavra_aux.index(letra.lower())
            palavra_aux[idx] = '_'
            palavra_revelada[idx] = letra.upper()
        
        print(palavra_revelada)
    
         





