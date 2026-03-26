from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

conteudo = Text()
valor = 0
conteudo.append("Iphone 17 Pro Max \n", )
conteudo.append("------------------------------ \n")
conteudo.append(f"----------R${valor}------------")

print(Panel(Align.center(conteudo), title="Banco", expand=False))