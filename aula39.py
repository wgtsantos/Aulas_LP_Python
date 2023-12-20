class Esporte:

    def __init__(self, nome):
        self.nome = nome
    
    def acao(self):
        pass
    
class Futebol(Esporte):
    
    def acao(self):
        return "Está jogando bola!"
    
class Natacao(Esporte):
    
    def acao(self):
        return "Está nadando em uma psicina!"