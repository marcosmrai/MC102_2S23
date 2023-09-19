import time
n = int(input("Digite um valor inteiro:"))

start = time.perf_counter()

i = 0
while i>n:
    print(i)
    i -= 1

i = 0
while i<n:
    print(i)
    i += 1
    
if n>0:
    print("Positiva")
elif n<0:
    print("Negativa")
    
print("Tempo de execução:", time.perf_counter()-start)