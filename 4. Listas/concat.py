a = [1, 2]
b = [3, 4]
c = a
c[len(c):len(c)] =b

c.append(5)

print(a)
print(b)
print(c)