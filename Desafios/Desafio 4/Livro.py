"""
Crie a classe Livro, que vai simular a pasasgem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura


o que deve contar no "self": titulo(nome do livro) e quantidade de paginas

SAÍDA: 
1. deve retornar a frase *"Voce acabou de abrir o livro "titulo do livro"* que tem X paginas no total. Voce agora está na *pagina 1*
2. quando acionada a função "avancar_paginas", deve retornar a quantidade de paginas passadas, uma por uma, e informar em que pagina o usuario se encontra
EX.: passei 4 paginas: Pag2  -> Pag3 -> Pag4 -> agora estou na Página 5
3. SE o livro tiver 20 paginas e eu avançar 50, vai percorrer ate a ultima pagina e depois retornará "Voce chegou ao final do livro "titulo do livro". mesmo se eu coloquei pra passar mais paginas do que tinha disponiel 


"""


class Livro:
    def __init__(self):
        pass