class FormatoBiscoito:
    def __init__(self):
        self.tamanho = 0
        self.massa = ""
        self.peso = 0

    # Outros Métodos 

    def BiscoitoPronto(self):
        return f"o seu biscoito ficou no tamanho {self.tamanho}cm, com a massa no sabor de {self.massa} e o peso de {self.peso}G "
    

biscoito1 = FormatoBiscoito()
biscoito1.tamanho = 8.5
biscoito1.massa = "Chocolate"
biscoito1.peso = 33.9

print(biscoito1.BiscoitoPronto())