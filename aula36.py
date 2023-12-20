def promo(opt, valor):
    
    descontos = { "a vista" : 0.10, "a prazo" : 0.04, "boleto" : 0.15 }
    
    if opt in descontos:
        
        desconto = descontos[opt]
        result = valor - (valor * desconto)
        return result
    
    else:
        return "Opção de desconto não encontrado!"
        

valor = float(input("Digite o valor da compra: "))

print("-" * 5 + "Escolha as opções de Desconto abaixo" + 5 * "-")
print("1. Pagamento a Vista -----")
print("2. Pagamento a Prazo -----")
print("3. Pagamento no Boleto -----")
print("-" * 20)

x =  int(input("=> "))

if x == 1:
    op = "a vista"
elif x == 2:
    op = "a prazo"
elif x == 3:
    op = "boleto"
else:
    op = ""
    
re = promo(op, valor)

if isinstance(re, str):
    print(re) 
else:  
    print(f"Escolhendo a opção {op} o valor final a pagar será de {re}")

    