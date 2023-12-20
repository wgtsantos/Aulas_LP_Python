idade = int( input("Informe sua idade: "))
resp = input("Possui CNH? sim ou não: ")
status = resp.lower()

check = True if status == "sim" else False

if idade >= 18:
    if check:
        print("Você pode dirigir um veiculo!")
    else:
        print("Você não pode Dirigir porque não possui CNH")
else:
    print("Você não tem idade para ter CNH e dirigir um veiculo!")