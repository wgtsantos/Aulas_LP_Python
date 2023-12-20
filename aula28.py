palavras = []
cont_a = 0
cont = 0

qtde = int(input("Quantas palavras deseja inserir: "))

for x in range(qtde):
    
    word = str(input(f"Digite um nome {x+1}: "))
    palavras.append(word)

for y in range(len(palavras)):
    
    if "a" in palavras[y]:
        
        cont_a += 1
        
    else:
        
        cont += 1
    
print("Palavras Cadastradas -----")

for p in palavras:
    print("=> " + p)
    
print("-" * 10)
print(f"Foram digitadas {cont_a} palavras que contém letra A.")
print(f"Foram digitadas {cont} palavras que não contém letra A.")