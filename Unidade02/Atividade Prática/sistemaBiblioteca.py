import matplotlib.pyplot as plt

class Livro:
    def __init__(self, titulo, autor, genero, quantidadeDisponivel):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidadeDisponivel = quantidadeDisponivel

listaLivros = Livro([])

print('Biblioteca de Livros')
resposta = input('Vamos cadastrar um novo livro (ou aperte S para sair)')

while resposta <= 'S':
    print('Cadastre um novo livro: \n')
    nomeLivro = input('Nome do livro:')