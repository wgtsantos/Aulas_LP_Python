def arred(x):
    return "%.2f" % x

def soma(a, b, c): 
    total = a + b + c
    return arred(total)

v1 = 3.50
v2 = 60.90
v3 = 45.99

print(soma(v1, v2, v3))