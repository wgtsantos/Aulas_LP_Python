# Conjuntos 

frutas = { "Banana", "Maçã", "Uva", "Jabuticaba", "Laranja", "Tomate" }

legumes = { "Cenoura", "Beterraba", "Abóbora", "Batata", "Tomate" }

sacola = frutas.union(legumes)
sacola2 = frutas.difference(legumes)
sacola3 = frutas.intersection(legumes)

frutas.add("Morango")

print(frutas)

lista_frutas = list(frutas)

print(lista_frutas[2])