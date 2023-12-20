valores = []

while True:
    
    valor = input("Informe um número ou digite 'sair' para encerrar: ")
    
    if valor.lower() == "sair":
        break
    
    valores.append(valor)
    
print("Valores Cadastrados " + "-" * 9)

valores.reverse() # inverter valores

for var in valores:
    print("=> " + var)