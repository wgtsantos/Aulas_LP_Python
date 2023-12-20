def saudacao(nome, sobrenome):
    print(f"Olá, {nome} {sobrenome}, seja Bem Vindo!")
    
def tempo(cidade, anos):
    total = 2023 - anos
    return f"Você mora em {cidade} faz {total} anos."
    
    
n = input("Informe seu nome: ")
s = input("Informe seu sobrenome: ")

c = input("Informe a sua cidade: ")
a = int(input(f"Em qual ano mudou para {c}?"))

saudacao(n,s)
print(tempo(c,a))