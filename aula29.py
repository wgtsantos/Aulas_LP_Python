doces = {}
chave = 0

while True:
    
    chave += 1
    
    doce = input("Informe o nome de um doce ou 'sair' para encerrar: ")
    doces[chave] = doce
    
    if doce.lower() == "sair":
        del doces[chave]
        break
    
for chave, doce in doces.items():
    
    print("ID: {} - Doce: {}".format(chave, doce))