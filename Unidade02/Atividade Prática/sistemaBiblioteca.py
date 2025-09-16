import matplotlib.pyplot as plt

class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Quantidade: {self.quantidade}'

listaLivros = ([])

def cadastrarLivro():
    print('--- Cadastro de Novo Livro ---')
    titulo = input('Título do livro: ')
    autor = input('Autor:')
    genero = input('Gênero literário: ')
    try:
        quantidade = int(input('Quantidade disponível: '))
        novoLivro = Livro(titulo, autor, genero, quantidade)
        listaLivros.append(novoLivro)
        print('\nLivro novo cadastrado!')
    except ValueError:
        print('\nErro: A quantidade deve ser um número inteiro.')

def listarLivros():
    print('\n Livros disponíveis:')
    if not listaLivros:
        print('Nenhum livro cadastrado até o momento...')
    else:
        for livro in listaLivros:
            print(livro)

def buscarPorTitulo():
    print('\n Buscar livro por título:')
    tituloBusca = input('Nome do livro:')
    encontrado = False

    for livro in listaLivros:
        if livro.titulo.lower() == tituloBusca.lower():
            print('\nLivro encontrado: ')
            print(livro)
            encontrado = True
            break
        if not encontrado:
            print(f'O livro "{tituloBusca}" não foi encontrado...')