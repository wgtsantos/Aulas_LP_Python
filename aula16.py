soma = 0

while True:
    
    valor = input("Digite um número ou 'sair' para encerrar: ")
    
    if valor.lower() == 'sair':
        break
    
    soma = soma + int(valor)   
      
print(f"A soma dos números digitados é: {soma}")