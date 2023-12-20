# Manipulações de textos
texto = "Python é uma linguagem de programação"

palavras = texto.split() # separar texto em palavras

print(palavras)

texto_junto = " ".join(palavras)

print(texto_junto)

texto_substituido = texto.replace("Python", "Java")

print(texto_substituido)

texto_maiusculo = texto.upper()
texto_minusculo = texto.lower()

print(texto_maiusculo + "\n" + texto_minusculo)

posicao = texto.find("linguagem")
print("A posição da palavra linguagem é: ", posicao)