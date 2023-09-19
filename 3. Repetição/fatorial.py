n = int(input("Entre com um número inteiro positivo: "))

#while n>1:
#    fat = fat*n
#    n = n-1
#    print(fat, n)
fat = 1
i = 0
print(i,fat)
while i<n:
    i = i+1
    fat = fat*i
    print(i,fat)

print("Fatorial:", fat)
    
