'''
criar uma classe "Churrasco" onde seja possivel informar:
1. quantas pessoas vao participar
2. mostre quanto de carne deve ser comprado
3. o custo total do churrasco
4. o preço por pessoa
CONSIDERE:
1. consumo padrao: 400g por pessoa
2. preço: R$82,40/kg

o que deve contar no "self": titulo(nome do churrasco) e quantidade de convidados

SAÍDA: deve fornecer um PANEL(rich) com a seguinte frase

analisando o Churras dos Amigos com X convidados
Recomendo comprar Xkg de carne 
o custo total será de R$X,xx
Cada pessoa pagará R$X,xx para participar
'''
from rich import print
from rich.panel import Panel

class ChurrasDosAmigos:
    #Método construtor acionado na instanciação
    def __init__(self, tituloDoEvento, quantidadeConvidados):
        self.tituloDoEvento = tituloDoEvento
        self.quantidadeConvidados = quantidadeConvidados

    
    # Métodos
    def analisar(self ):
        self.RecomendacaoQuantidadeCarne = 0.400 * self.quantidadeConvidados
        self.custoTotal = 82.40 * self.RecomendacaoQuantidadeCarne
        self.custoPorPessoa = self.custoTotal / self.quantidadeConvidados

        print(Panel(f"Analisando o [green]{self.tituloDoEvento}[/green] com [blue]{self.quantidadeConvidados}[/blue] convidados.\nCada Participante comerá 0.4Kg e cada Kg custa R$82.40.\nRecomendo comprar [blue]{self.RecomendacaoQuantidadeCarne}kg[/blue] de carne.\nO custo total será de [green]R${self.custoTotal:.2f}[/green].\nCada pessoa pagará [yellow]R${self.custoPorPessoa}[/yellow] para participar", width=70, title=self.tituloDoEvento) )
        
teste = ChurrasDosAmigos("Churras Dos Amigos", 20)
teste.analisar()
