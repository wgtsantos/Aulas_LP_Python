pessoas = {
          "Erick" : { "Telefone" : "(31) 98653-7623", "Idade" : 16, "Time" : "Atlético-MG"},
          "Alice" : { "Telefone" : "(31) 98534-2211", "Idade" : 16, "Time" : "Cruzeiro" },
          "Yuri" : { "Telefone" : "(31) 99976-3142", "Idade" : 19, "Time" : "Atlético-MG" },
          "Robson" : { "Telefone" : "(31) 99764-5662", "Idade:" : 25, "Time" : "Vila Nova"},
          "Bernardo" : { "Telefone:" : "(31) 96548-5007", "Idade" : 30, "Time" : "Atlético-MG"},
          "Maria Eduarda" : { "Telefone" : "(31) 97543-3131", "Idade:" : 20, "Time" : "Atlético-MG"}  
        }

def buscar_pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} : {valor}")

nome_busca = input("Digite o nome da pessoa que deseja buscar: ")

if nome_busca in pessoas:
    detalhes = pessoas[nome_busca]
    print(f"Informações de {nome_busca} ---------------")
    buscar_pessoa(**detalhes)
else:
    print(f"{nome_busca} não foi encontrado nos resgistros!")