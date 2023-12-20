from aula38 import Produto

# p = Produto("Maria", 130, 5)
p = Produto()

p.nome = "Feijão"
p.valor = 130.00
p.qtde = 5

print(f"Comprando {p.qtde} unidades de {p.nome} pelo valor de R${p.valor} você ira pagar o total de R$ {p.total()}")