# Argumentos empacotados
def arred(x):
    return "%.2f" % x

def soma(*args):
    total = 0
    for num in args:
        total += num
    return total

def media(*args):
    total = cont = 0
    for x in args:
        total += x
        cont += 1
    return arred(total/cont)

valores = [23, 10, 6, 8, 17, 55]

result = soma(*valores)
m = media(*valores)

print(result)
print(m)
    