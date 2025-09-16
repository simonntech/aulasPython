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

#Gerar gráfico

def gerarGraficoGenero():
    if not listaLivros:
        print('\nNão há livros cadastrados.')
        return
    
    quantidadeGeneros = {}

    for livro in listaLivros:
        genero = livro.genero.capitalize()
        quantidadeGeneros[genero] = quantidadeGeneros.get(genero, 0) + 1

    generos = list(quantidadeGeneros.keys())
    quantidades=list(quantidadeGeneros.values())

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