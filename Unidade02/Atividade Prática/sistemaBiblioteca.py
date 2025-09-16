#importando a biblioteca Matplotlib para gerar os gráficos
import matplotlib.pyplot as plt

#criação da classe livro, com as propriedades do título, autor, gênero e quantidade
class Livro:
    #função construtora das propriedades
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    #função para escrever as informações do Livro
    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Quantidade: {self.quantidade}'

#lista de livros como lista vazia
listaLivros = []

#função para cadastrar Livros
def cadastrarLivro():
    print('--- Cadastro de Novo Livro ---')
    titulo = input('Título do livro: ')
    autor = input('Autor:')
    genero = input('Gênero literário: ')

    #condicional para tentar cadastrar o livro, caso esteja com as informações válidas
    try:
        quantidade = int(input('Quantidade disponível: '))
        novoLivro = Livro(titulo, autor, genero, quantidade)
        listaLivros.append(novoLivro)
        print('\nLivro novo cadastrado!')
    #tratamento de erro da condicional
    except ValueError:
        print('\nErro: A quantidade deve ser um número inteiro.')

#função para listar os livros
def listarLivros():
    print('\n Livros disponíveis:')
    if not listaLivros:
        print('Nenhum livro cadastrado até o momento...')
    else:
        for livro in listaLivros:
            print(livro)

#função para buscar livro pelo título
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

#Gerar gráfico
def gerarGraficoGenero():
    #condicional caso não tenha livros na lista
    if not listaLivros:
        print('\nNão há livros cadastrados.')
        return
    
    #iniciar gêneros vazios
    quantidadeGeneros = {}

    for livro in listaLivros:
        genero = livro.genero.capitalize()
        quantidadeGeneros[genero] = quantidadeGeneros.get(genero, 0) + 1

    generos = list(quantidadeGeneros.keys())
    quantidades=list(quantidadeGeneros.values())

    #propriedades do gráfico
    plt.figure(figsize=(10,6))
    plt.bar(generos, quantidades, color='skyblue')
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade de livros')
    plt.title('Quantidade de livros por Gênero')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


# função principal
def main():
    #looping que retorna algo de acordo com a opção selecionada pelo usuário
    while True:
        print('\n --- Sistema Biblioteca ---')
        print('1. Cadastrar novo Livro')
        print('2. Listar Livros')
        print('3. Buscar livro')
        print('4. Gerar gráfico de livros por gênero')
        print('5. Sair')

        escolha = input('Digite sua escolha (1-5):')

        if escolha == '1':
            cadastrarLivro()
        elif escolha == '2':
            listarLivros()
        elif escolha == '3':
            buscarPorTitulo()
        elif escolha == '4':
            gerarGraficoGenero()
        elif escolha == '5':
            print('Fechando sistema.')
            break
        else:
            print('Escolha inválida. Por favor, digite um número entre 1 a 5 das opções.')

if __name__ == '__main__':
    main()