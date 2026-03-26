'''
Desafio usando a biblioteca RICH para formatação mais vizualmente atrativo
consiste em apenas montar um programa onde recebe certas informações de funcionarios e coloca numa frase ficticia
'''


from rich import print
class Funcionarios:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self):
        return f":handshake: Ola, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo"
        
c1 = Funcionarios("Maria", "Administração", "Diretora")
print(c1.apresentacao())


c2 = Funcionarios("Pedro", "TI", "Programador")
print(c2.apresentacao())
