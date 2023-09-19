frutas = "Frutas: {0}, {1} e {2}"
print(frutas.format("abacaxi", "banana", "caqui"))
# Frutas: abacaxi , banana e caqui
pets = "Quem é mais inteligente: {1} ou {0}?"
print(pets.format("gato", "cachorro"))
# Quem é mais inteligente: cachorro ou gato?


s = []

s.append("Um")
s.append("Dois")
s.append("Três")
    
# later
    
s = '  vem antes do  '.join(s)

print(s)

string = "    3.134,\t 43254,- 9.4343, \t  +0.4232\n"
print(string)
print(string.replace(" ", "").replace("\t", "(tinha uma tabulacao aqui)"))
#print([float(value) for value in string.replace(" ", "").split(",")])
#print(string.strip().split(","))
#print([value.strip() for value in string.strip().split(",")])
#print([float(value) for value in string.strip().split(",")])