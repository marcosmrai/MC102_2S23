def primeiros_primos(n):
    pp = []
    i = 2
    while len(pp)<n:
        if eh_primo(i):
            pp.append(i)
        i+=1
    
    return pp

def eh_primo(x):
    '''
    Função que calcula se um um inteiro é primo

            Parameters:
                    x (int): Um número inteiro

            Returns:
                    eh_primo (bool): True se é primo, false se não é primo
    '''
    primo = True
    if x % 2 == 0:
        return False
    for divisor in range(3, int(x**0.5)+1, 2):
        if x % divisor == 0:
            return False

    return True

#n = int(input("Entre com um número inteiro positivo: "))
#pp = primeiros_primos(n)
#print(pp)

while True:
    n = int(input("Entre com um número inteiro positivo: "))
    if eh_primo(n):
        print("Ele é primo.")
        break
    else:
        print("Ele não é primo.")