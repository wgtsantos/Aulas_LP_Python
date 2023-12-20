nota1 = float( input("Informe a nota 1: "))
nota2 = float( input("Informe a nota 2: "))
nota3 = float( input("Informe a nota 3: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")