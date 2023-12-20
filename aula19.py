maiorvalor = 0
menorvalor = float('inf')
total = 0

for x in range(4): 
    
    valor = int(input("Informe um número: "))   
    
    total += valor
       
    if valor > maiorvalor:
        
        maiorvalor = valor
       
    if valor < menorvalor:
        
        menorvalor = valor

print("O menor valor é: ", menorvalor)
print("O maior valor é: ", maiorvalor)