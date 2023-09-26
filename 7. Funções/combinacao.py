def fat(a):
    if a<0:
        print("Coloca um valor positivo aê.")
    elif a == 1 or a == 0:
        return 1
    else:
        return a*fat(a-1)

'''
def fat(a):
    var_fat = 1
    for i in range(2,a+1):
        var_fat*=i
    return var_fat
'''

def combinatorial(a, b):
    return fat(a)/(fat(a-b)*fat(b))

print(combinatorial(10, 2))