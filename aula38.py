class Produto:
    
    # def __init__(self, nome, valor, qtde):
        
    #     self.nome = nome
    #     self.valor = valor
    #     self.qtde = qtde
        
    def _init__(self):
        self.__nome = None
        self.__valor = 0
        self.__qtde = 0
    
    def nome(self):
        return self.__nome
    
    def valor(self):
        return self.__valor
    
    def qtde(self):
        return self.__qtde
    
    def total(self):
        
        total = self.valor * self.qtde
        return total