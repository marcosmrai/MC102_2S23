'''
a = "Python"
b = "Py" + "thon"
c = "p" + "ython"
print(a == b)
# True
print(a.lower() == c.lower())
# False
print(b != c)
# True

print("thor" in a)

comp = "Py"
print(a.startswith("Py"))
print(a[:len(comp)] == comp)

idx = a.find("hor")

print(idx)
if idx >= 0:
    print(a[idx:])
'''

print([value.isnumeric() for value in "teste 123".split()])