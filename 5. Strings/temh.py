while True:
    palavra = input('Digite uma palavra: ')
    if palavra == "":
        break
    elif 'h' in palavra.lower():
        print('Tem H')
    else:
        print('Não tem H')