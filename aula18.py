soma = 0

num = int(input("Informe um número ou digite -1 para sair: "))

while num != -1:
    
   if num > 10:
       
       soma = soma + int(num)
    
   num = int(input("Informe um número ou digite -1 para sair: "))  
       
print("O valores digitados maiores que 10 foram somados")
print("O total final é: ", soma)