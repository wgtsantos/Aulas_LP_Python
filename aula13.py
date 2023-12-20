print("-" * 10 + " MENU " + "-" * 10)
print("Escolha uma opção abaixo: " + "-" * 5)
print("1. Somar " + "-" * 8)
print("2. Subtrair " + "-" * 8)
print("3. Multiplicar " + "-" * 8)
print("4. Dividir " + "-" * 8)
print("-" * 15 + "-" * 15)

def calc(opt):
    match opt:
        case 1:
            num1 = int(input("Informe o primeiro número: "))
            num2 = int(input("Informe o segundo número: "))
            soma = num1 + num2
            return f"O resultado da soma é {soma}"
        case 2:
            num1 = int(input("Informe o primeiro número: "))
            num2 = int(input("Informe o segundo número: "))
            sub = num1 - num2
            return sub
        case 3:
            num1 = int(input("Informe o primeiro número: "))
            num2 = int(input("Informe o segundo número: "))
            mult = num1 * num2
            return mult
        case 4: 
            num1 = float(input("Informe o primeiro número: "))
            num2 = float(input("Informe o segundo número: "))
            div = num1 / num2
            return div
        case _:
            return "Valor Inválido"

resp = int(input("=> "))
print(calc(resp))

        