ai_2 = int(input("Digite um termo: "))
ai_1 = int(input("Digite um termo: "))
N = int(input("Digite o número de termos: "))

print("0-ésimo termo:", ai_2)
print("1-ésimo termo:", ai_1)

for i in range(2,N):
    #print(i, ai_1, ai_2)
    if i%2 == 1:
        ai = ai_1+ai_2
    else:
        ai = ai_1-ai_2
    print(str(i)+"-ésimo termo:", ai)
    ai_2 = ai_1
    ai_1 = ai
